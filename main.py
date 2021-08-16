import requests
from bs4 import BeautifulSoup
import time
import pandas as pd


item_list = []

for x in range (1,10):
    url = 'https://www.kawanlama.com/solutions/informa.html?p='
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    }

    r = requests.get(url+str(x), headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    content = soup.find_all('div', {'class': 'product-item-info'})
    for item in content:
        try:
            brand = item.find('div', {'class': 'brand_name'}).text.strip()
            title = item.find('a', {'class': 'product-item-link'}).text.strip()
            sku = item.find('p', {'class': 'sku-number'}).text.strip()
            price = item.find('span', {'class': 'price'}).text
        except:
            brand = 'none'
            title = 'none'
            sku = 'none'
            price = 'none'

        item_info = {
            'brand': brand,
            'title': title,
            'sku': sku,
            'price': price
        }

        item_list.append(item_info)
        time.sleep(2)
        print('product found: ',len(item_list))

df = pd.DataFrame(item_list)
print(df.head)
df.to_csv('kawanlama.csv')
df.to_json('kawanlama.json')
