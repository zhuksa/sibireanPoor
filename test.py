import requests
from bs4 import BeautifulSoup


# https://lenta.ru/news/2019/08/10/ranen/

class Article(object):
    def __init__(self, h, p):
        self.h = h
        self.p = p

    def get_text(self):
        return self.h + self.p


class Parser(object):
    def __init__(self, url):
        self.url = url
        print(self.url)

    def parse(self):
        soup = BeautifulSoup(requests.get(self.url).content, 'html.parser')
        h1 = soup.find('h1').text
        paragraphs = ''
        for p in soup.findAll('p'):
            for a in p.findAll('a'):
                a.replace_with(p.a.string + ' URL:[' + p.a.get('href') + ']')
            paragraphs = paragraphs + p.get_text() + '\n\n'
        article = Article(h1.center(200) + '\n', paragraphs)
        print(paragraphs)
        file = File(h1 + '.txt')
        file.save(article.get_text())


class File(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def save(self, text):
        file = open(self.file_name, 'w+')
        file.write(text)
        file.close()


class Dictionary(object):
    def __init__(self, template):
        self.template = {'width': 80, "indent": 2, 'url': 'True'}


my_parser = Parser(input())
my_parser.parse()
