import asyncio
import codecs
import datetime as dt
import os, sys
from sqlite3 import DatabaseError
from django.contrib.auth import get_user_model

proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ["DJANGO_SETTINGS_MODULE"] = "scraping_service.settings"

import django
django.setup()

from scraping.parsers import *
from scraping.models import Vacancy, City, Language, Error, Url



RealUser = get_user_model()

parsers = (
    (superjob, 'superjob'),
    (careerist, 'careerist'),
    (jooble, 'jooble')
)

jobs, errors = [], []

def get_settings():
    # qs = RealUser.objects.filter(send_email=True).values()
    qs = RealUser.objects.all().values()
    setting_list = set((q['city_id'], q['language_id']) for q in qs)
    return setting_list

def get_urls(_settings):
    qs = Url.objects.all().values()
    url_dict = {(q['city_id'], q['language_id']): q['url_data'] for q in qs}
    urls = []
    for pair in _settings:
        if pair in url_dict:
            tmp = {}
            tmp['city'] = pair[0]
            tmp['language'] = pair[1]
            tmp['user_url_data'] = url_dict[pair]
            urls.append(tmp)
    return urls

async def main(value):
    func, url, city, language = value
    job, err = await loop.run_in_executor(None, func, url, city, language)
    errors.extend(err)
    jobs.extend(job)



settings = get_settings()
url_list = get_urls(settings)


# city = City.objects.filter(slug='sаnkt-peterburg').first()
# language = Language.objects.filter(slug='golang').first()



loop = asyncio.get_event_loop()
tmp_tasks = [(func, data['user_url_data'][key], data['city'], data['language'])
             for data in url_list
             for func, key in parsers]
tasks = asyncio.wait([loop.create_task(main(f)) for f in tmp_tasks])

# for data in url_list:
#     for func, key in parsers:
#         url = data['user_url_data'][key]
#         j, e = func(url, city=data['city'], language=data['language'])
#         jobs += j
#         errors += e

loop.run_until_complete(tasks)
loop.close()

for job in jobs:
    v = Vacancy(**job)
    try:
        v.save()
    except DatabaseError:
        pass

if errors:
    qs = Error.objects.filter(timestamp=dt.date.today())
    if qs.exists():
        err = qs.first()
        err.data.update({'errors': errors})
        err.save()
    else:
        er = Error(data=f'errors: {errors}').save()


ten_days_ago = dt.date.today() - dt.timedelta(10)
Vacancy.objects.filter(timestamp__lte=ten_days_ago).delete()



# h = codecs.open('work.txt', 'w', 'utf-8')
#
# for i in range(len(jobs)):
#     h.write(str(jobs[i]))
#     h.write(str('\n'))
# h.close()


# h.write(str(jobs))
# h.close()


