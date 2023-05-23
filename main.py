from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup


url = "https://forms.office.com/e/jaTv4JAzPG"

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

driver.get(url)
driver.maximize_window()

#DOES NOT WAIT FOR URL TO CONTAIN GIVEN STRING
WebDriverWait(driver, 10).until(EC.url_contains("forms.office.com"))

print("yeah babe")

print(ChromeDriverManager().install())

#Get html and parse it 

# html = driver.page_source
# soup = BeautifulSoup(html, "html.parser")

# print(soup.get_text())