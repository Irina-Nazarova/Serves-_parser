import requests
from bs4 import BeautifulSoup


URL = 'https://www.avito.ru/moskva/koshki/poroda-abissinskaya-ASgBAgICAUSoA_QU?cd=1'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36', 'accept': '*/*'}
HOST = 'https://www.avito.ru'

def get_html(url, params=None):
    """ Функция для получения контента с указанного url."""
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='iva-item-root-G3n7v photo-slider-slider-3tEix '
                                        'iva-item-list-2_PpT iva-item-redesign-1OBTh '
                                        'items-item-1Hoqq items-listItem-11orH js-catalog-item-enum')
    cats = []
    for item in items:
        price = item.find('span', class_='price-root-1n2wM price-listRedesign-2OaSA')
        if price:
            price = price.get_text()
        else:
            price = 'Цену уточняйте'
        cats.append({
            'title': item.find('a', class_='link-link-39EVK link-design-default-2sPEv '
                                           'title-root-395AQ iva-item-title-1Rmmj '
                                           'title-listRedesign-3RaU2 '
                                           'title-root_maxHeight-3obWc').get_text(),
            'link': HOST + item.find('a', class_='link-link-39EVK link-design-default-2sPEv '
                                           'title-root-395AQ iva-item-title-1Rmmj '
                                           'title-listRedesign-3RaU2 '
                                           'title-root_maxHeight-3obWc').get('href'),
            'price': item.find('span', class_='price-root-1n2wM price-listRedesign-2OaSA').get_text(),
        })
    print(cats)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        return 'Error'


parse()


