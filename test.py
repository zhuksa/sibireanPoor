import requests #импорт библиотеки 'Request'-иммитатор http-запросов
from bs4 import BeautifulSoup as bs # импорт -позволяет распарсить ответ полученный от сервера

headers = {'accept': '*/*',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'} #иммуляция введения браузера

base_url = 'https://lenta.ru/news/2019/08/10/ranen/' #ссылка откуда парсим

def lenta_parse(base_url, headrs): # создание функции
    session = requests.Session() # создание сессии
    request = session.get(base_url, headers=headers) #иммуляция открытия страницы в браузере
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser') #результат работы BeautifulSoup, котороая в свою очередь принимает request.content- весь ответ который отправляет сервер, html.parser-встроенный парсер в python, который позволяет разбивать ответ сервера на блоки html страницы
        h1 = soup.find ('h1').text
        divs = soup.find_all ('div', attrs={'class':'b-text clearfix js-topic__text'})
        #for div in divs:
            #title = div.find('p').text

        file = open('text.txt', 'w')

        print(file.name)
        file.write(h1)
        file.close()

        print(file.closed)



        print (h1.center(150))
        print(divs)
    else:
        print ('ERROR')



lenta_parse (base_url, headers)
