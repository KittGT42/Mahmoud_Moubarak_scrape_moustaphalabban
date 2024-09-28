import csv
import requests
from bs4 import BeautifulSoup
from lxml import etree
import json
from datetime import datetime

headers_csv = ['Product_ID', 'Product_Name', 'Product_Barcode', 'Product_Sku', 'Product_Attribute_color', 'Product_Attribute_size',
               'Product_Descriptions', 'Product_Categorise', 'Product_Price', 'Product_Sale_price', 'Product_Image']

today_day_data = f'_{datetime.now().day}_{datetime.now().month}_{datetime.now().year}'
with open(f'detailed_info_product{today_day_data}.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers_csv)
counter = 0
for number_page in range(1, 65):
    response = requests.get(
        f'https://moustaphalabban.com/collections/all?page={number_page}',
    )
    soup_page = BeautifulSoup(response.text, 'lxml')
    all_links_in_page = soup_page.find_all('div', class_='product-block__inner')
    for link in all_links_in_page:
        link = 'https://moustaphalabban.com' + link.find('a').get('href')
        response_page_detail = requests.get(link).text

        # Парсим содержимое файла как HTML
        tree = etree.HTML(response_page_detail)

        # Ищем первый тег <script> с типом application/json
        script_tag = tree.xpath('//script[@type="application/json"]/text()')

        # Если нашли, парсим как JSON
        if json.loads(script_tag[-1]):
            json_data = json.loads(script_tag[-1])
            soup = BeautifulSoup(json_data['description'], 'html.parser')
            text_descriptions = soup.get_text(separator="\n")
            for data_info in json_data['variants']:
                counter += 1
                Product_ID = data_info['id']
                Product_Name = data_info['name']
                Product_Barcode = data_info['barcode']
                Product_Sku = data_info['sku']
                Product_Attribute_color = data_info['option1']
                Product_Attribute_size = data_info['option2']
                Product_Descriptions = text_descriptions
                Product_Categorise = json_data['tags']
                Product_Price = str(json_data['compare_at_price'])[:-2] + '.' + str(json_data['compare_at_price'])[-2:]
                Product_Sale_price = str(json_data['price'])[:-2] + '.' + str(json_data['price'])[-2:]
                try:
                    Product_Image = data_info['featured_image']['src'][2:]
                except:
                    try:
                        Product_Image = json_data['images'][0][2:]
                    except:
                        Product_Image = 'None'

                with open(f'detailed_info_product{today_day_data}.csv', 'a', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow([Product_ID, Product_Name, Product_Barcode, Product_Sku, Product_Attribute_color, Product_Attribute_size,
                                     Product_Descriptions, Product_Categorise, Product_Price, Product_Sale_price, Product_Image])
                print(f'Page-{number_page} #{counter} name-{Product_Name} / {3145}')
        else:
            print(f'Page-{number_page} #{counter} name-{Product_Name} / {3145}')