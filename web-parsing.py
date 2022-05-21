import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

f = open('goods.csv', 'w', newline='\n', encoding='utf-8')
file = csv.writer(f)
file.writerow(['name', 'description', 'total in stock', 'price', 'discount'])
page = 1

while page <= 5:
    url = 'https://onoff.ge/super-price?OrderBy=30&DiscountRanges=30-&PageNumber=' + str(page)
    request = requests.get(url)
    html = BeautifulSoup(request.text, features='html.parser')
    products = html.find_all('div', class_='product-item')

    for product in products:
        name = product.find('h2', class_='header-medium').a.text.strip()
        description = product.find('p', class_='text-regular').text.strip()
        totalInStock = product.find('button', class_='text-medium').i.text.strip()
        price = product.find('i', class_='GEL').previous_sibling.text.strip()
        discount = product.find('p', class_='new-min-super-price').text.strip()
        print(name, description, price, discount)
        file.writerow([name, description, totalInStock, price, discount])
    page += 1
    sleep(randint(15, 20))
# print(request)
# print(request.status_code)
# content = request.text
# print(content)