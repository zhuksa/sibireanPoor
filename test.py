from requests import Session
from bs4 import BeautifulSoup as bs

HEADERS = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                         'Chrome/76.0.3809.100 Safari/537.36'}

BASE_URL = str(input('Введите ссылку на статью:_'))  #'https://lenta.ru/news/2019/08/10/ranen/'


def lenta_parse(BASE_URL, HEADERS):
    req = Session().get(BASE_URL, headers=HEADERS)
    if req.status_code == 200:
        soup = bs(req.content, 'html.parser')
        h1 = soup.find('h1').text
        print(h1.center(150))
        all_p = soup.findAll('p')
        for p in all_p:
            pizdez = p.get_text()
            print(pizdez)
        file = open('text.txt', 'w')
        print(file.name)
        file.write(h1.center(200) + '\n')
        for p in all_p:
            file.write(p.get_text() + '\n')
        file.close()
    else:
        print('ERROR')


lenta_parse(BASE_URL, HEADERS)
