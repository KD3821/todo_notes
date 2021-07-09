import requests
import codecs
from bs4 import BeautifulSoup as BS


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept':'text/html,application/xhtml+xml,applicatio/xml;q=0.9,*/*;q=0.8'
}




def superjob(url):
    jobs = []
    errors = []
    domain = 'https://spb.superjob.ru'
    url = 'https://spb.superjob.ru/vacancy/search/?keywords=python'
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        main_div = soup.find('div', attrs={'class': '_1ID8B'})
        if main_div:
            div_lst = main_div.find_all('div', attrs={'class': 'iJCa5 f-test-vacancy-item _1fma_ _2nteL'})
            for div in div_lst:
                title = div.find('div', attrs={'class': '_1h3Zg _2rfUm _2hCDz _21a7u'})
                href = title.a['href']
                title_name = title.a.text
                company = div.find('span', attrs={'class': '_1h3Zg _3Fsn4 f-test-text-vacancy-item-company-name e5P5i _2hCDz _2ZsgW _2SvHc'})
                company_name = company.a.text
                description = div.find('span', attrs={'class': '_1h3Zg _38T7m e5P5i _2hCDz _2ZsgW _2SvHc'})
                content = description.text

                jobs.append({'title': title_name,
                             'url': domain+href,
                             'description': content,
                             'company': company_name})
        else:
            errors.append({'url': url, 'title': "Div does not exist"})
    else:
        errors.append({'url': url, 'title': "Page does not response"})

    return jobs, errors


def careerist(url):
    jobs = []
    errors = []
    domain = 'https://spb.careerist.ru'
    url = 'https://spb.careerist.ru/jobs-python/'
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        main_div = soup.find('div', attrs={'class': 'vacSearchList'})
        if main_div:
            div_lst = main_div.find_all('div', attrs={'class': 'list send-res-from-catalog-container'})
            for div in div_lst:
                title = div.find('p', attrs={'class': 'h5 card-text'})
                href = title.a['href']
                title_name = title.a.text
                company = div.find('div', attrs={'class': 'm-b-10'})
                company_name = company.a.text
                d = div.find('div', attrs={'class': 'list-block'})
                description = d.find_all('p', attrs={'class': 'card-text'})
                for element in description:
                    if element.get_text():
                        content = element.text

                jobs.append({'title': title_name,
                             'url': href,
                             'description': content,
                             'company': company_name})
        else:
            errors.append({'url': url, 'title': "Div does not exist"})
    else:
        errors.append({'url': url, 'title': "Page does not response"})

    return jobs, errors


if __name__ == '__main__':
    url = 'https://spb.careerist.ru/jobs-python/'
    jobs, errors = careerist(url)
    h = codecs.open('work.txt', 'w', 'utf-8')
    for i in range(len(jobs)):
        h.write(str(jobs[i]))
        h.write(str('\n'))
    h.close()
