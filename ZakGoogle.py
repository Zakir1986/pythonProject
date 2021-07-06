# В этом скрипте пользователь задает ключевое слово, по которому
# скачиваются ссылки из выдачи Google, и потом по каждой ссылке проверяете, хороший у нее title или
# плохой.

from requests_html import HTMLSession
from PreferenseTitle import title_quality

#
# keywords = input('Введите ключевое слово: ')
#
#
# def take_position(keywords):
#     session = HTMLSession()
#     resp = session.get(f'https://www.google.com/'f'search?q={keywords}&num=100&hl=en')
#     serp = resp.html.xpath('//*[@id="rso"]/div/div/div/div[1]/a/@href')
#
#     for position, link in enumerate(serp, 1):
#         print(title_quality(link))
#
#
# print(take_position(keywords))




# Скрипт в итоге подсчитывает и выводит на экран количество сайтов в TOP-100, которые находятся на протоколе http и https

keywords = input('Введите ключевое слово: ')

list_http = {}
list_https = {}


def take_position(keywords):
    session = HTMLSession()
    resp = session.get(f'https://www.google.com/'f'search?q={keywords}&num=100&hl=en')
    serp = resp.html.xpath('//*[@id="rso"]/div/div/div/div[1]/a/@href')

    for position, link in enumerate(serp, 1):
        # print(position, link)
        if (link.split('/')[0]) == 'http:':
            list_http[position] = link
            # print(position, link)
        else:
            list_https[position] = link
            # continue

    print(list_https)
    print(list_http)



# Функция которая на вход принимает ключевое слово и название домена. А на выходе возвращает позицию домена по этому
# слову.

# def take_position(keyword='Фонбет: вопросы и ответы',
#                   domain='https://bookmaker-ratings.ru/wiki-category/bk-voprosy-i-otvety/faq-fonbet/'):
#     session = HTMLSession()
#     resp = session.get(f'https://www.google.com/'f'search?q={keyword}&num=100&hl=en')
#     serp = resp.html.xpath('//*[@id="rso"]/div/div/div/div[1]/a/@href')
#     for position, link in enumerate(serp, 1):
#         if domain in link:
#             return position
#     return 'Not Found'
# print(take_position())
