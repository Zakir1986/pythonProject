import requests
from bs4 import BeautifulSoup
from list import list
import re

# Наличие текста в начале и в конце списка
for url in list:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    description_below = soup.find('div', class_='description-below')
    desc = soup.find('div', class_='description')
    if description_below is None:
        description_below = 0
    else:
        description_below = 1

    if desc is None:
        desc = 0
    else:
        desc = 1
    print(url, desc, ' | ', description_below)