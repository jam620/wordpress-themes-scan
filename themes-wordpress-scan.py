#!/usr/local/bin/python3
# _*_ coding: utf8 _*_

import requests
from bs4 import BeautifulSoup


def test():
    agent = {'User-Agent': 'Firefox'}
    peticion = requests.get(url="https://pnaw4.morenojose.com/", headers=agent)
    soup = BeautifulSoup(peticion.text, 'html.parser')
    #lo añadi para ver que devolvia
    #print(soup)
    for enlace in soup.find_all('link'):
    #    print(enlace)
        if '/wp-content/themes/' in enlace.get('href'):
            the = enlace.get('href')
            the = the.split('/')
            if 'themes' in the:
                pos = the.index('themes')
                theme = the[pos + 1]
                print("Tema en uso: " + theme)
                return True


if __name__ == '__main__':
    test()
