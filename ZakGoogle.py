from requests_html import HTMLSession

def take_position(keyword='Фонбет: вопросы и ответы', domain='https://bookmaker-ratings.ru/wiki-category/bk-voprosy-i-otvety/faq-fonbet/'):
    session = HTMLSession()
    resp = session.get(f'https://www.google.com/'f'search?q={keyword}&num=100&hl=en')
    serp = resp.html.xpath('//*[@id="rso"]/div/div/div/div[1]/a/@href')
    for position, link in enumerate(serp, 1):
        if domain in link:
            return position
    return 'Not Found'


print(take_position())
