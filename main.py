from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import time


url = "https://forms.office.com/e/jaTv4JAzPG"

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

driver.get(url)
driver.maximize_window()

#We have to wait on first operation cuz when login page is loading url actually contains "https://forms.office.com"
while True:
    time.sleep(1) #TO CHANGE ON FIRST ITERATION TO WAIT FOR LOADING PAGE NOT JUST 1 S
    if driver.current_url.startswith("https://forms.office.com"):
        time.sleep(2) #TO CHANGE TO WAIT FOR PAGE TO LOAD NOT JUST 2 S
        break

#now get html and parse it 
