import requests
import bs4
import pprint

pp = pprint.PrettyPrinter(indent=4)
test_print = True


def get_it(url):
    item = requests.get(url).json()
    return item

def get_it_testing(url, item_title, item_type):
    item = requests.get(url).json()
    if test_print:
        cprinter(item_title, item, item_type)
    return item

def cprinter(item_title, items, item_type):
    print(f'\n↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ {item_title} ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓')
    if item_type=='list':
        for item in items:
            pp.pprint(item)
    elif item_type=='dict':
        pp.pprint(items)
    print(f'↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑S↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ {item_title} ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑\n')