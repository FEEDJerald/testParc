import requests
import csv
BASE_URL = 'https://4lapy.ru'
API = '/api/goods_list_cached/'
SORT = 'popular'
CATEGORY_ID = 165
PAGE = 1
TOKEN = '002838b6fd9dcd6df6aba30f517549dd'
SIGN = '1fe01a20bc55634b1cac0b6b5529d9a0'
all_dict = []
while True:
    try:
        response = requests.get(f"{BASE_URL}{API}?sort={SORT}&category_id={CATEGORY_ID}&page={PAGE}&count=10&token={TOKEN}&sign={SIGN}",headers={'Cookie':'selected_city_code=0000073738'})
        result = response.json()
        for counter in range(0,10):
            ids = result['data']['goods'][counter]['id']
            title = result['data']['goods'][counter]['title']
            webpage = result['data']['goods'][counter]['webpage']
            basePrice = result['data']['goods'][counter]['price']['old']
            actualPrice = result['data']['goods'][counter]['price']['actual']
            brand_name = result['data']['goods'][counter]['brand_name']
            avi = result['data']['goods'][0]['isAvailable']
            if avi == True:
                if basePrice == 0:
                    basePrice = actualPrice
                all_dict.append({"id товара":ids,
                                 "наименование": title,
                                 "ссылка на товар": webpage,
                                 "регулярная цена" : basePrice,
                                 "промо цена": actualPrice,
                                 "бренд": brand_name})
        PAGE += 1
    except:
        print(PAGE)
        break
with open ("Moscow.csv","w",encoding='utf-8-sig') as file:
    writer = csv.DictWriter(file,fieldnames={"id товара","наименование","ссылка на товар","регулярная цена","промо цена", "бренд"})
    writer.writeheader()
    writer.writerows(all_dict)
BASE_URL = 'https://4lapy.ru'
API = '/api/goods_list_cached/'
SORT = 'popular'
CATEGORY_ID = 165
PAGE = 1
TOKEN = '002838b6fd9dcd6df6aba30f517549dd'
SIGN = '27939f3be1cd7edde00f5d5451c749df'
all_dict = []
while True:
    try:
        response = requests.get(f"{BASE_URL}{API}?sort={SORT}&category_id={CATEGORY_ID}&page={PAGE}&count=10&token={TOKEN}&sign={SIGN}",headers={'Cookie':'selected_city_code=0000073738'})
        result = response.json()
        for counter in range(0,10):
            ids = result['data']['goods'][counter]['id']
            title = result['data']['goods'][counter]['title']
            webpage = result['data']['goods'][counter]['webpage']
            basePrice = result['data']['goods'][counter]['price']['old']
            actualPrice = result['data']['goods'][counter]['price']['actual']
            brand_name = result['data']['goods'][counter]['brand_name']
            avi = result['data']['goods'][0]['isAvailable']
            if avi == True:
                if basePrice == 0:
                    basePrice = actualPrice
                all_dict.append({"id товара":ids,
                                 "наименование": title,
                                 "ссылка на товар": webpage,
                                 "регулярная цена" : basePrice,
                                 "промо цена": actualPrice,
                                 "бренд": brand_name})
        PAGE += 1
    except:
        print(PAGE)
        break
with open ("SPB.csv","w",encoding='utf-8-sig') as file:
    writer = csv.DictWriter(file,fieldnames={"id товара","наименование","ссылка на товар","регулярная цена","промо цена", "бренд"})
    writer.writeheader()
    writer.writerows(all_dict)