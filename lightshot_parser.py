import requests
from bs4 import BeautifulSoup

import random

import string

import time

import os

import json

import urllib3
import urllib.request

def main():
    http = urllib3.PoolManager()
    url = 'https://prnt.sc/ujaclu'
    
    q = str(random.choice(string.ascii_letters))
    w = str(random.choice(string.ascii_letters))
    e = str(random.choice(string.ascii_letters))
    r = str(random.choice(string.ascii_letters))
    t = str(random.choice(string.ascii_letters))
    y = str(random.choice(string.ascii_letters))
    
    url = q + w + e + r + t + y
    url = url.lower()
    print(url)
    
    
    f = open('lightshot_images_list.txt', 'r')
    a = f.read()
    while url in a:
        url = 'https://prnt.sc/ujaclu'
    
        q = str(random.choice(string.ascii_letters))
        w = str(random.choice(string.ascii_letters))
        e = str(random.choice(string.ascii_letters))
        r = str(random.choice(string.ascii_letters))
        t = str(random.choice(string.ascii_letters))
        y = str(random.choice(string.ascii_letters))

        url = q + w + e + r + t + y
        url = url.lower()
        
    f.close()
    f = open('lightshot_images_list.txt', 'a')
    f.write(url)
    f.write(' ')
    f.close()

        
    
    realurl = 'https://prnt.sc/poopy'
    realurl = realurl.replace('poopy', url)
    
    r = http.request('GET', realurl)
    
    if r.status == 200:
        soup = BeautifulSoup(r.data, 'lxml')
        picture_url = soup.find_all('img', class_='no-click screenshot-image')

        picture_url = str(picture_url)
        picture_url = picture_url.replace('[<img alt="Lightshot screenshot" class="no-click screenshot-image" crossorigin="anonymous" id="screenshot-image" image-id="', '')
        picture_url = picture_url.replace(url, '')
        picture_url = picture_url.replace('" src="', '')
        picture_url = picture_url.replace('"/>]', '')

        print(picture_url)

        r = http.request('GET', picture_url)

        print(r.status)
        
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join('c:LightShot')

        
        with open(os.path.expanduser(os.path.join("~/Desktop/Lightshot",url + ".png")), "wb") as file:
            file.write(r.data)
    else:
        print('url не существует')
    
    

while True:
    main()