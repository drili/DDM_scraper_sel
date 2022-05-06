# Python scraper for DDM ("https://detdanskemadhus.dk/bestil-privat"), using Selenium & bs4.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import bs4

print("sample test case started")
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\kynet\Desktop\Python\Kunder\DDM\scraper\Browsers\chromedriver.exe")
driver.get("https://detdanskemadhus.dk/bestil-privat")
try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "products"))
    )
finally:
    html_content = driver.page_source
    soup = bs4.BeautifulSoup(html_content)
    h3_tags = soup.find_all("h3")
    h3_tags_array = []
    for h3 in h3_tags:
            h3_tags_array.append(h3)
            print(h3)
    
    # with open('test.txt', 'w') as myFile:
    #     myFile.write(h3_tags_array)
    driver.quit()