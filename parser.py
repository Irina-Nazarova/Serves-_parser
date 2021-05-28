import requests
from bs4 import BeautifulSoup
import csv
import os

URL = 'https://www.avito.ru/moskva/koshki/poroda-abissinskaya-ASgBAgICAUSoA_QU?cd=1'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36', 'accept': '*/*'}
HOST = 'https://www.avito.ru'
FILE = 'cats.csv'


def get_html(url, params=None):
    """ Функция для получения контента с указанного url."""
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('span', class_='pagination-item-1WyVp')
    if len(pagination[1:-1]) > 0:
        return len(pagination[1:-1])
    else:
        return 1


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='iva-item-root-G3n7v photo-slider-slider-3tEix '
                                        'iva-item-list-2_PpT iva-item-redesign-1OBTh '
                                        'items-item-1Hoqq items-listItem-11orH js-catalog-item-enum')
    cats = []
    for item in items:
        price = item.find('span', class_='price-root-1n2wM price-listRedesign-2OaSA')
        if price:
            price = price.get_text().replace(u'\xa0', u' ')
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
            'price': price,
            'metro': item.find('div', class_='geo-root-1pUZ8 iva-item-geo-1Ocpg').get_text().replace(u'\xa0', u' '),
        })
    return cats


def save_file(items, path):
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter =';')
        writer.writerow(['Порода', 'Ссылка', 'Цена в руб.', 'Метро'])
        for item in items:
            writer.writerow([item['title'], item['link'], item['price'], item['metro']])


def parse():
    URL = input('Введите URL: ')
    URL = URL.strip()
    html = get_html(URL)
    if html.status_code == 200:
        cats = []
        pages_count = get_pages_count(html.text)
        for page in range(1, pages_count + 1):
            print(f' Парсинг страницы {page} из {pages_count}...')
            html = get_html(URL, params={'page': page})
            cats.extend(get_content(html.text))
        save_file(cats, FILE)
        print(f' Получено {len(cats)} котиков')
        os.startfile(FILE)
    else:
        return 'Error'


parse()


