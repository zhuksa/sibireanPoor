import requests
from bs4 import BeautifulSoup
from json import loads
from textwrap import fill
from os import makedirs


class Article(object):
    def __init__(self, h, p):
        self.h = h
        self.p = p

    def get_text(self):
        return self.h + self.p


class Parser(object):
    def __init__(self, url):
        self.url = url
        self.conf = Conf()

    def parse(self):
        soup = BeautifulSoup(requests.get(self.url).content, 'html.parser')
        h1 = soup.find('h1').text
        paragraphs = []
        for p in soup.findAll('p'):
            for a in p.findAll('a'):
                a.replace_with(p.a.string + ' URL:[' + p.a.get('href') + ']')
            paragraphs.append(fill(p.get_text(), self.conf.width) + '\n' * self.conf.indent)
        article = Article(h1.center(80) + '\n', ''.join(paragraphs))
        file = File(h1 + '.txt', self.url)
        file.save(article.get_text())


class File(object):
    def __init__(self, file_name, url):
        self.file_name = file_name
        self.url = url

    def save(self, text):
        file_path = self.url.lstrip('https://').lstrip('http://')
        makedirs(file_path)
        file = open(file_path + 'index.txt', 'w+')
        file.write(text)
        file.close()


class Conf(object):
    def __init__(self):
        file = open('settings.txt', 'r')
        conf = loads(str(file.read()))
        self.width = conf['width']
        self.indent = conf['indent']
        file.close()


my_parser = Parser(input())
my_parser.parse()
