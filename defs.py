# def create_google_link(keyword, google='www.google.ru/'):
#     link = f'https://{google}/search?q={keyword}&num=100&hl=en'
#     return link

import requests
from bs4 import BeautifulSoup
from list import list
import re

# Наличие FAQ на странице в HTML коде по маркеру - <div itemtype = 'https://schema.org/FAQPage'>
for url in list:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    description_below = soup.find('div', class_='description-below')
    description = soup.find('div', class_='description')
    if description_below is None:
        description_below = 0
    else:
        description_below = 1

    if description is None:
        description = 0
    else:
        description = 1
print(description,' | ', description_below)

    # Ерархия заголовков, а в каком варианте представить данные? Такой пойдет?

    list = []
    for tag in soup.find_all(re.compile('^h[1-6]$')):
        res = tag.name
        list.append(res)
    if ('h2' and 'h3') not in list:
        H = f'Внимание!{list}'
    else:
        H = f'{list}'

        # # Наличие видео на странице по маркеру - https://player.vimeo.com/
        #
        # items = soup.find('iframe')
        # if items is None:
        #     print('Video', url, 0)
        # else:
        #     print('Video', url, 1)

        # Наличие фильтров на странице по маркеру - filters-container

    items = soup.find('div', class_='filters-container')
    if items is None:
        FiltersK = 'Filters 0 |'
    else:
        FiltersK = 'Filters 1 |'

    print(url, FAQ, FiltersK, H)
