# Домашнее задание по уроку 3: для Title страницы, считаем количество слов, символов, уникальных слов.
# Анализируем хороший Title или плохой по любым параметрам

# Коментарии к реализации: Title парсится с введенного URL. Анализируется существование тега <title> и наличие
# нескольких тегов <title>. Интересно было бы сделать правильный вариант ввода, спарсить заголовок,
# если он существует и обработать. Пока не совсем  понял обработку Try/Except  поэтому реализовал иначе. P.S. при
# редиректах парсит Title конечной страницы. При 404 парсит заголовок 404.

from requests_html import HTMLSession


def title_quality(url):
    # Список рекомендаций по Title, пока пустой
    recomendation = []
    session = HTMLSession()
    try:
        resp = session.get(url)
    except:
        print('Ошибка')
        title_html = None
    else:
        # Парсим страницу и ищем тег <title>
        title_html = resp.html.xpath('//title')

    # Обработку Title проводим только если есть такой тег и только первый.
    if title_html:
        title = title_html[0].text
        # Считаем символы
        count_chars = len(title)
        # Удаляем изи тайтла все лишние символы: () - = / \ ! ? | + _ . : ; 	« » , & а дефисы заменены на пробелы
        title1 = title.replace('(', '')
        title1 = title.replace(')', '')
        title1 = title.replace('=', '')
        title1 = title.replace('-', ' ')
        title1 = title.replace('/', '')
        title1 = title.replace('/', '\\')
        title1 = title.replace('!', '')
        title1 = title.replace('?', '')
        title1 = title.replace('|', '')
        title1 = title.replace('+', '')
        title1 = title.replace('_', '')
        title1 = title.replace('.', '')
        title1 = title.replace(':', '')
        title1 = title.replace(';', '')
        title1 = title.replace('«', '')
        title1 = title.replace('»', '')
        title1 = title.replace(',', '')
        title1 = title.replace('&', '')

        # Считаем все слова в отфармотированом Тайтле
        list_title = title1.split()
        count_words = len(list_title)

        # Считаем количество уникальных слов
        unique_words = len(set(list_title))

        # Анализ качества Тайтл
        # Качество на несколько тегов Title
        if len(title_html) > 1:
            recomendation.append('На странице присутствует больше одного тега Title, рекомендуется оставить только '
                                 'первый')

        # Качество на количество символов
        if count_chars == 0:
            recomendation.append('Title пустой, рекомендуется заполнить тег')
        elif 0 < count_chars < 20:
            recomendation.append('Title выглядит коротким, рекомендуется добавить больше символов')
        elif 70 < count_chars:
            recomendation.append('В Title более 70 символов, рекомендуется сделать короче')
        else:
            recomendation.append('Title имеет приемлемое количество символов')

        # Качество на количество слов
        if 0 < count_words < 3:
            recomendation.append('В Title менее 3 слов, это мало')
        elif 3 <= count_words < 5:
            recomendation.append('Title выглядит коротким, рекомендуется добавить больше слов')
        elif 5 <= count_words < 14:
            recomendation.append('В Title приемлемое количество слов')
        else:
            recomendation.append('Title имеет много слов')

        # Качество на повторяющиеся слова
        if count_words > 0 and count_words == unique_words:
            recomendation.append('Все слова в Title уникальны')
        elif count_words > 0 and (count_words - unique_words) >= 1:
            recomendation.append('В Title есть повторяющиеся слова')

        # Качество Title на пассажи
        if ('?' in title) or ('.' in title) or ('!' in title):
            recomendation.append('Title разбит на пассажи')

        # Выводим информацию по Title
        print(f'Title:{title}\n')
        print(f'Количество символов в Title:{count_chars}')
        print(f'Количество слов в Title:{count_words}')
        print(f'Количество уникальных слов в Title:{unique_words}')
    else:
        recomendation.append(f'На странице отсутствует тег <title>, либо не удалось загрузить странцу: {url}')

    # Вывод рекомендаций по Title в консоль

    print('\n Рекомендации по Title:')
    for i, item in enumerate(recomendation):
        print(i + 1, ') ', item)



