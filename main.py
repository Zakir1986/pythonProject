import requests
from bs4 import BeautifulSoup
# from list import list
from LsitTest import ListTetst
import re


for url in ListTetst:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    cont = soup.find('div', class_='content-middle')
    if cont is None:
        print(url, 'Другой шаблон')
        continue
    buttons = cont.find_all('a', class_='button')
    line = []
    for item in buttons:
        line.append(item.string)
    print(url, line)

# # Обьем текста # # Обьем текста
#     textContainer = soup.find('div', class_='seo-text-container').text
#     textNameAsList = textContainer.split(' ')  # текст в тип список
#
# # Количество символов
#     listAsStr = ''
#     for i in textNameAsList:
#         listAsStr += i
#     characters = len(listAsStr)
#     replaceText = listAsStr.replace(' ', '')
#     # количество слов в тексте
#     wordCount = len(textNameAsList)
#
#
#     # Актуальные бонусы
#     bonusActual = soup.find('div', attrs={'v-html': 'bonusActualHtml'})
#     bonusActualCards = bonusActual.find_all('div', class_='bonus-card')
#     i = 0
#     for tag in bonusActualCards:
#         i +=1
#     resActual = str(i)
#
#
#     # Другие бонусы
#     bonusOtherHtml = soup.find('div', attrs={'v-html': 'bonusOtherHtml'})
#     bonusOtherCards = bonusOtherHtml.find_all('div', class_='bonus-card')
#     i = 0
#     for tag in bonusOtherCards:
#         i +=1
#     resOther = str(i)
#
#     # Прошедшие акции
#     bonusArchiveHtml = soup.find('div', attrs={'v-html': 'bonusArchiveHtml'})
#     bonusArhivCards = bonusArchiveHtml.find_all('div', class_='bonus-card')
#     i = 0
#     for tag in bonusArhivCards:
#         i +=1
#     resArhive = str(i)
#
#     print(url, '|', resActual, '|', resOther, '|', resArhive, '|', characters, '|', wordCount)







