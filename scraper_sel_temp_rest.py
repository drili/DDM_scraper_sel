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

print("sample test case started")
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

array_all = []
array_associative_all = {"Title":[], "ID":[]}

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
    array_associative_hovedretter = dict()
    for product in products[0]:
        iterator += 1
        product_array_data = []
        
        title = product.find('h3').contents[0].strip()
        data_entity_id = product["data-entity-id"]
        data_url = product["data-url"]
        price = product.find("span", {"class": "integer"}).contents[0].strip()
        thumbnail = product.find("div", {"class": "image"})["style"]
        thumbnail_formatted = re.findall("'([^']*)'", thumbnail)
        current_week = datetime.datetime.now().isocalendar()[1]
        category = "Hovedretter"
        product_array_data.extend([title,data_entity_id,data_url,price,thumbnail_formatted[0],current_week,category])
        array_all_hovedretter.append(product_array_data)

        array_associative_all["Title"].append(title)
        array_associative_all["ID"].append(data_entity_id)
        # array_associative_all["title"] = title
        # array_associative_all["data_entity_id"] = data_entity_id
        # array_associative_all["data_url"] = data_url
        # array_associative_all["price"] = price
        # array_associative_all["thumbnail_formatted"] = thumbnail_formatted[0]
        # array_associative_all["current_week"] = current_week
        # array_associative_all["category"] = category
        
    array_all.append(array_all_hovedretter)
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
            product_array_data = []

            title = product.find('h3').contents[0].strip()
            data_entity_id = product["data-entity-id"]
            data_url = product["data-url"]
            price = product.find("span", {"class": "integer"}).contents[0].strip()
            thumbnail = product.find("div", {"class": "image"})["style"]
            thumbnail_formatted = re.findall("'([^']*)'", thumbnail)
            current_week = datetime.datetime.now().isocalendar()[1]
            category = "Forretter"
            product_array_data.extend([title,data_entity_id,data_url,price,thumbnail_formatted[0],current_week,category])
            array_all_forretter.append(product_array_data)

        # with open('test.txt', 'w') as myFile:
        #     myFile.write(h3_tags_array)
        array_all.append(array_all_forretter)
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
                product_array_data = []

                title = product.find('h3').contents[0].strip()
                data_entity_id = product["data-entity-id"]
                data_url = product["data-url"]
                price = product.find("span", {"class": "integer"}).contents[0].strip()
                thumbnail = product.find("div", {"class": "image"})["style"]
                thumbnail_formatted = re.findall("'([^']*)'", thumbnail)
                current_week = datetime.datetime.now().isocalendar()[1]
                category = "Desserter"
                product_array_data.extend([title,data_entity_id,data_url,price,thumbnail_formatted[0],current_week,category])
                array_all_desserter.append(product_array_data)

            # with open('test.txt', 'w') as myFile:
            #     myFile.write(h3_tags_array)
            array_all.append(array_all_desserter)
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
                    product_array_data = []

                    title = product.find('h3').contents[0].strip()
                    data_entity_id = product["data-entity-id"]
                    data_url = product["data-url"]
                    price = product.find("span", {"class": "integer"}).contents[0].strip()
                    thumbnail = product.find("div", {"class": "image"})["style"]
                    thumbnail_formatted = re.findall("'([^']*)'", thumbnail)
                    current_week = datetime.datetime.now().isocalendar()[1]
                    category = "Familiepakker"
                    product_array_data.extend([title,data_entity_id,data_url,price,thumbnail_formatted[0],current_week,category])
                    array_all_familiepakker.append(product_array_data)
                    
                # with open('test.txt', 'w') as myFile:
                #     myFile.write(h3_tags_array)
                array_all.append(array_all_familiepakker)
                driver_familiepakker.quit()
                # print(array_all)
                print(array_associative_all)