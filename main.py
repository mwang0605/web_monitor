from bs4 import BeautifulSoup

import requests

import time

import random

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

#url='https://mwang0605.github.io/esports_website/'

url="https://www.centurycommunities.com/find-your-home/georgia/dalton-metro/jefferson/oconee-station"

response = requests.get(url, headers=headers)

origin_html = response.text


random_int = random.randint(0,10)
# soup = BeautifulSoup(html, "html5lib")
#
# text = soup.get_text(strip=True)

#print (origin_html)

while 1:
    new_response = requests.get(url, headers=headers)

    new_html = new_response.text

    if origin_html == new_html:
        print("no changes")
        time.sleep(10 + random_int)
    else:
        print("website changed")
        print(origin_html,"||||||||||", new_html)
        exit()