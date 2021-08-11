import requests
import codecs
from bs4 import BeautifulSoup as BS


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
           }


jobs = []
errors = []
domain = 'https://ru.jooble.org'
url = 'https://ru.jooble.org/SearchResult?rgns=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3&ukw=python'
resp = requests.get(url, headers=headers)
if resp.status_code == 200:
    soup = BS(resp.content, 'html.parser')
    main_div = soup.find('div', attrs={'class': 'Content_content__18fg4'})
    if main_div:
        div_lst = main_div.find_all('article', attrs={'class', 'JobCard_card__FxQpv JobList_card__yKsad'})
        for div in div_lst:
            title = div.find('h2', attrs={'class': 'JobCard_position_heading__15V35'})
            href = title.a['href']
            title_name = title.a.text
            company = div.find('div', attrs={'class': 'GoodEmployerWidget_employer__1JrOt JobCard_employer_widget__3mz-P'})
            company_name = company.text
            description = div.find('div', attrs={'class': 'JobCard_description__9jGwm'})
            content = description.span.text
            jobs.append({'title': title_name,
                         'url': href,
                         'description': content,
                         'company': company_name})
    else:
        errors.append({'url': url, 'title': "Div does not exist"})
else:
    errors.append({'url': url, 'title': "Page does not response"})


h = codecs.open('jooble.txt', 'w', 'utf-8')
for i in range(len(jobs)):
    h.write(str(jobs[i]))
    h.write(str('\n'))
h.close()
