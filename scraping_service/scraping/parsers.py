import requests
import codecs
from bs4 import BeautifulSoup as BS
from random import randint


__all__ = ('superjob', 'careerist', 'jooble')


headers = [
    {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/53.0',
     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    ]



def superjob(url, city=None, language=None):
    jobs = []
    errors = []
    domain = 'https://spb.superjob.ru'
    if url:
        resp = requests.get(url, headers=headers[randint(0, 2)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            new_jobs = soup.find('h1', attrs={'class': '_1h3Zg _1TK9I _2hCDz _2ZsgW'})
            if not new_jobs:
                main_div = soup.find('div', attrs={'class': '_1ID8B'})
                if main_div:
                    div_lst = main_div.find_all('div', attrs={'class': 'Fo44F QiY08 LvoDO'})
                    for div in div_lst:
                        title = div.find('div', attrs={'class': '_1h3Zg _2rfUm _2hCDz _21a7u'})
                        href = title.a['href']
                        title_name = title.a.text
                        company = 'No name'
                        comp = div.find('span', attrs={'class': '_1h3Zg _3Fsn4 f-test-text-vacancy-item-company-name e5P5i _2hCDz _2ZsgW _2SvHc'})
                        if comp:
                            company = comp.a.text
                        description = div.find('span', attrs={'class': '_1h3Zg _38T7m e5P5i _2hCDz _2ZsgW _2SvHc'})
                        content = description.text

                        jobs.append({'title': title_name,
                                     'url': domain+href,
                                     'description': content,
                                     'company': company,
                                     'city_id': city,
                                     'language_id': language})
                else:
                    errors.append({'url': url, 'title': "Div does not exist"})
            else:
                errors.append({'url': url, 'title': "Page is empty"})
        else:
            errors.append({'url': url, 'title': "Page does not response"})

    return jobs, errors



def careerist(url, city=None, language=None):
    jobs = []
    errors = []
    domain = 'https://spb.careerist.ru'
    if url:
        resp = requests.get(url, headers=headers[randint(0, 2)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            new_jobs = soup.find('p', attrs={'class': 'lead'})
            if not new_jobs:
                main_div = soup.find('div', attrs={'class': 'vacSearchList'})
                if main_div:
                    div_lst = main_div.find_all('div', attrs={'class': 'list send-res-from-catalog-container'})
                    for div in div_lst:
                        title = div.find('p', attrs={'class': 'h5 card-text'})
                        href = title.a['href']
                        title_name = title.a.text
                        company = 'No name'
                        comp = div.find('div', attrs={'class': 'm-b-10'})
                        if comp:
                            company = comp.a.text
                        d = div.find('div', attrs={'class': 'list-block'})
                        description = d.find_all('p', attrs={'class': 'card-text'})
                        for element in description:
                            if element.get_text():
                                content = element.text

                        jobs.append({'title': title_name,
                                     'url': href,
                                     'description': content,
                                     'company': company,
                                     'city_id': city,
                                     'language_id': language})
                else:
                    errors.append({'url': url, 'title': "Div does not exist"})
            else:
                errors.append({'url': url, 'title': "Page is empty"})
        else:
            errors.append({'url': url, 'title': "Page does not response"})

    return jobs, errors



def jooble(url, city=None, language=None):
    jobs = []
    errors = []
    domain = 'https://ru.jooble.org'
    if url:
        resp = requests.get(url, headers=headers[randint(0, 2)])
        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            new_jobs = soup.find('div', attrs={'class': 'NoResultTitle_noresult__title__1wmQl'})
            if not new_jobs:
                main_div = soup.find('div', attrs={'class': 'Content_content__18fg4'})
                if main_div:
                    div_lst = main_div.find_all('article', attrs={'class', 'JobCard_card__FxQpv JobList_card__yKsad'})
                    for div in div_lst:
                        title = div.find('h2', attrs={'class': 'JobCard_position_heading__15V35'})
                        href = title.a['href']
                        title_name = title.a.text
                        company = 'No name'
                        comp = div.find('div', attrs={'class': 'GoodEmployerWidget_employer__1JrOt JobCard_employer_widget__3mz-P'})
                        if comp:
                            company = comp.text
                        description = div.find('div', attrs={'class': 'JobCard_description__9jGwm'})
                        content = description.text
                        jobs.append({'title': title_name,
                                     'url': href,
                                     'description': content,
                                     'company': company,
                                     'city_id': city,
                                     'language_id': language})
                else:
                    errors.append({'url': url, 'title': "Div does not exist"})
            else:
                errors.append({'url': url, 'title': "Page is empty"})
        else:
            errors.append({'url': url, 'title': "Page does not response"})

    return jobs, errors


if __name__ == '__main__':
    url = 'https://ru.jooble.org/SearchResult?rgns=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3&ukw=python'
    jobs, errors = jooble(url)
    h = codecs.open('work.txt', 'w', 'utf-8')
    for i in range(len(jobs)):
        h.write(str(jobs[i]))
        h.write(str('\n'))
    h.close()