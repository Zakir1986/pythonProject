import requests
from bs4 import BeautifulSoup
from list import list
import re

#
for url in list:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    bookmakers_rating_table = soup.find('div', class_='bookmakers-rating-table')
    if bookmakers_rating_table is None:
        print(url, ' Attention!')
        continue
    desc = bookmakers_rating_table.find_all('div', class_='table-row')

    print(url, ' | ', len(desc))



    # if description_below is None:
    #     description_below = 0
    # else:
    #     description_below = 1
    #
    # if desc is None:
    #     desc = 0
    # else:
    #     desc = 1

    # print(url, desc, ' | ', description_below)