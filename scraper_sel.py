# Python scraper for DDM ("https://detdanskemadhus.dk/bestil-privat"), using Selenium & bs4.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
import bs4
import re
import time
import json

print("sample test case started")
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

array_all = []

### Hovedretter
driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\kynet\Desktop\Python\Kunder\DDM\scraper\Browsers\chromedriver.exe")
driver.get("https://detdanskemadhus.dk/bestil-privat#hovedretter")
try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "products"))
    )
finally:
    print("::: success finding element (hovedretter)")
    
    html_content = driver.page_source
    soup = bs4.BeautifulSoup(html_content, "html.parser")
    products = soup.select(".products.piranya-grid")
    # print(products)
    
    iterator = 0
    array_all_hovedretter = []
    for product in products[0]:
        iterator += 1
        array_associative_hovedretter = {"id":[], "url":[], "title":[], "price":[], "thumbnail":[], "large_image":[], "week":[], "category":[]}
        title = product.find('h3').contents[0].strip()
        data_entity_id = product["data-entity-id"]
        data_url = product["data-url"]
        price = product.find("span", {"class": "integer"}).contents[0].strip()
        thumbnail = product.find("div", {"class": "image"})["style"]
        thumbnail_formatted = re.findall("'([^']*)'", thumbnail)
        current_week = datetime.datetime.now().isocalendar()[1]
        category = "Hovedretter"
        # product_array_data.extend([title,data_entity_id,data_url,price,thumbnail_formatted[0],current_week,category])
        # array_all_hovedretter.append(product_array_data)

        array_associative_hovedretter["id"].append(data_entity_id)
        array_associative_hovedretter["url"].append(data_url)
        array_associative_hovedretter["title"].append(title)
        array_associative_hovedretter["price"].append(price)
        array_associative_hovedretter["thumbnail"].append(thumbnail_formatted[0])
        array_associative_hovedretter["large_image"].append(thumbnail_formatted[0])
        array_associative_hovedretter["week"].append(current_week)
        array_associative_hovedretter["category"].append(category)
        
        array_all.append(array_associative_hovedretter)
    driver.quit()
    # with open('test.txt', 'w') as myFile:
    #     myFile.write(h3_tags_array)

    ### Forretter
    driver_forretter = webdriver.Chrome(options=options, executable_path=r"C:\Users\kynet\Desktop\Python\Kunder\DDM\scraper\Browsers\chromedriver.exe")
    driver_forretter.get("https://detdanskemadhus.dk/bestil-privat#forretter")
    try:
        element = WebDriverWait(driver_forretter, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "products"))
        )
    finally:
        print("::: success finding element (forretter)")
        
        html_content = driver_forretter.page_source
        soup = bs4.BeautifulSoup(html_content, "html.parser")
        products = soup.select(".products.piranya-grid")
        
        iterator = 0
        array_all_forretter = []
        for product in products[1]:
            iterator += 1
            array_associative_forretter = {"id":[], "url":[], "title":[], "price":[], "thumbnail":[], "large_image":[], "week":[], "category":[]}
            title = product.find('h3').contents[0].strip()
            data_entity_id = product["data-entity-id"]
            data_url = product["data-url"]
            price = product.find("span", {"class": "integer"}).contents[0].strip()
            thumbnail = product.find("div", {"class": "image"})["style"]
            thumbnail_formatted = re.findall("'([^']*)'", thumbnail)
            current_week = datetime.datetime.now().isocalendar()[1]
            category = "Forretter"
            # product_array_data.extend([title,data_entity_id,data_url,price,thumbnail_formatted[0],current_week,category])
            # array_all_hovedretter.append(product_array_data)

            array_associative_forretter["id"].append(data_entity_id)
            array_associative_forretter["url"].append(data_url)
            array_associative_forretter["title"].append(title)
            array_associative_forretter["price"].append(price)
            array_associative_forretter["thumbnail"].append(thumbnail_formatted[0])
            array_associative_forretter["large_image"].append(thumbnail_formatted[0])
            array_associative_forretter["week"].append(current_week)
            array_associative_forretter["category"].append(category)

            array_all.append(array_associative_forretter)
        driver_forretter.quit()
    
        ### Desserter
        driver_desserter = webdriver.Chrome(options=options, executable_path=r"C:\Users\kynet\Desktop\Python\Kunder\DDM\scraper\Browsers\chromedriver.exe")
        driver_desserter.get("https://detdanskemadhus.dk/bestil-privat#desserter")
        try:
            element = WebDriverWait(driver_desserter, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "products"))
            )
        finally:
            print("::: success finding element (desserter)")
            
            html_content = driver_desserter.page_source
            soup = bs4.BeautifulSoup(html_content, "html.parser")
            products = soup.select(".products.piranya-grid")

            iterator = 0
            array_all_desserter = []
            for product in products[2]:
                iterator += 1
                array_associative_desserter = {"id":[], "url":[], "title":[], "price":[], "thumbnail":[], "large_image":[], "week":[], "category":[]}
                title = product.find('h3').contents[0].strip()
                data_entity_id = product["data-entity-id"]
                data_url = product["data-url"]
                price = product.find("span", {"class": "integer"}).contents[0].strip()
                thumbnail = product.find("div", {"class": "image"})["style"]
                thumbnail_formatted = re.findall("'([^']*)'", thumbnail)
                current_week = datetime.datetime.now().isocalendar()[1]
                category = "Desserter"
                # product_array_data.extend([title,data_entity_id,data_url,price,thumbnail_formatted[0],current_week,category])
                # array_all_hovedretter.append(product_array_data)

                array_associative_desserter["id"].append(data_entity_id)
                array_associative_desserter["url"].append(data_url)
                array_associative_desserter["title"].append(title)
                array_associative_desserter["price"].append(price)
                array_associative_desserter["thumbnail"].append(thumbnail_formatted[0])
                array_associative_desserter["large_image"].append(thumbnail_formatted[0])
                array_associative_desserter["week"].append(current_week)
                array_associative_desserter["category"].append(category)

                array_all.append(array_associative_desserter)
            driver_desserter.quit()

            ### Familiepakker
            driver_familiepakker = webdriver.Chrome(options=options, executable_path=r"C:\Users\kynet\Desktop\Python\Kunder\DDM\scraper\Browsers\chromedriver.exe")
            driver_familiepakker.get("https://detdanskemadhus.dk/bestil-privat#familiepakker")
            try:
                element = WebDriverWait(driver_familiepakker, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "products"))
                )
            finally:
                print("::: success finding element (familiepakker)")
                
                html_content = driver_familiepakker.page_source
                soup = bs4.BeautifulSoup(html_content, "html.parser")
                products = soup.select(".products.piranya-grid")

                iterator = 0
                array_all_familiepakker = []
                for product in products[3]:
                    iterator += 1
                    array_associative_familiepakker = {"id":[], "url":[], "title":[], "price":[], "thumbnail":[], "large_image":[], "week":[], "category":[]}
                    title = product.find('h3').contents[0].strip()
                    data_entity_id = product["data-entity-id"]
                    data_url = product["data-url"]
                    price = product.find("span", {"class": "integer"}).contents[0].strip()
                    thumbnail = product.find("div", {"class": "image"})["style"]
                    thumbnail_formatted = re.findall("'([^']*)'", thumbnail)
                    current_week = datetime.datetime.now().isocalendar()[1]
                    category = "Familiepakker"
                    # product_array_data.extend([title,data_entity_id,data_url,price,thumbnail_formatted[0],current_week,category])
                    # array_all_hovedretter.append(product_array_data)

                    array_associative_familiepakker["id"].append(data_entity_id)
                    array_associative_familiepakker["url"].append(data_url)
                    array_associative_familiepakker["title"].append(title)
                    array_associative_familiepakker["price"].append(price)
                    array_associative_familiepakker["thumbnail"].append(thumbnail_formatted[0])
                    array_associative_familiepakker["large_image"].append(thumbnail_formatted[0])
                    array_associative_familiepakker["week"].append(current_week)
                    array_associative_familiepakker["category"].append(category)

                    array_all.append(array_associative_familiepakker)
                driver_familiepakker.quit()
                # print(array_all)
                print(array_all)

                ### Serializing json
                # json_object = json.dumps(array_all, indent = 1) 

                ### Create JSON file and import data
                with open("testfile.json", "w") as f:
                    f.write(json.dumps(array_all, separators=(',', ': ')))
                    print("::: JSON file created & data dumped.")
                    # print(json_object)
    