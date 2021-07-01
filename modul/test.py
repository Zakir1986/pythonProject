def create_google_link(keyword, google='www.google.ru/'):
    link = f'https://{google}/search?q={keyword}&num=100&hl=en'
    return link