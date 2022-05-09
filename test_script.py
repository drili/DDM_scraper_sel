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
    for product in products[2]:
        print(product)
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
        print(title)
        print(data_entity_id)
        print(data_url)
        print(price)
        print(thumbnail_formatted[0])
        print(current_week)
        print(category)
    
    # with open('test.txt', 'w') as myFile:
    #     myFile.write(h3_tags_array)
    driver_desserter.quit()