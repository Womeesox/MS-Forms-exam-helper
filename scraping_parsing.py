from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import time

def scrape_form(url):
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

    html = driver.page_source
    return html

def parse_questions(html):
    soup = BeautifulSoup(html, "html.parser")

    question_list_div = soup.find('div', id='question-list')
    questions = question_list_div.find_all("div", {"data-automation-id": "questionItem"})

    #get all questions as dict
    questions_dict = dict()
    for question in questions:
        questions_dict[question.find("span", {"data-automation-id": "questionTitle"}).get_text()] = question.find_all("div", {"data-automation-id": "choiceItem"})

    #parse answers
    for question in questions_dict:
        for count, answer in enumerate(questions_dict[question], 0):
            questions_dict[question][count] = questions_dict[question][count].get_text()
    #to check wtf is this. After first answer there's some wird "\xa0" in my output and in html "&nbsp;"
    #and this in html isn't showing
    return questions_dict

example_url = "https://forms.office.com/e/jaTv4JAzPG"

print(parse_questions(scrape_form(example_url)))
