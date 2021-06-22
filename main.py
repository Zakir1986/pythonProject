import requests
from bs4 import BeautifulSoup
# from list import list
from LsitTest import ListTetst
import re
f = open('text.txt', 'w')
for url in ListTetst:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    result = re.findall(r'https://player.vimeo.com/video/', str(soup))

    if not result:
        Video = 0
    else:
        Video = 1

    items = soup.find('div', attrs={'itemtype': 'https://schema.org/FAQPage'})
    if items is None:
        FAQ = 0
    else:
        FAQ = 1

    listTag = []
    for tag in soup.find_all(re.compile('^h[1-6]$')):
        res = tag.name
        listTag.append(res)
    if ('h2' and 'h3') not in listTag:
        hierarchy = f'Внимание!{listTag}'
    else:
        hierarchy = f'{listTag}'
    print(url, '|', Video, '|', FAQ, '|', hierarchy)
    f.write(url + '|' + str(Video) + '|' + str(FAQ) + '|' + hierarchy)
f.close()


