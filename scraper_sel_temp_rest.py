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

array_all = {"item":[]}

### Hovedretter
driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\Drilon Braha\Desktop\Python\KYNETIC\DDM_selscraper\scraper\Browsers\chromedriver.exe")
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
        array_associative_hovedretter = {}
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

        array_associative_hovedretter.update({"id": data_entity_id})
        array_associative_hovedretter.update({"url": data_url})
        array_associative_hovedretter.update({"title": title})
        array_associative_hovedretter.update({"price": price})
        array_associative_hovedretter.update({"thumbnail": "https://detdanskemadhus.dk/"+thumbnail_formatted[0]})
        array_associative_hovedretter.update({"large_image": "https://detdanskemadhus.dk/"+thumbnail_formatted[0]})
        array_associative_hovedretter.update({"week": current_week})
        array_associative_hovedretter.update({"category": category})
        
        array_all["item"].append(array_associative_hovedretter)
    driver.quit()
    # with open('test.txt', 'w') as myFile:
    #     myFile.write(h3_tags_array)
    print(array_all)
    
    ### Create JSON file and import data
    with open("testfile.json", "w", encoding='utf8') as f:
        f.write(json.dumps(array_all, separators=(',', ': ')))
        print("::: JSON file created & data dumped.")
        # print(json_object)
    