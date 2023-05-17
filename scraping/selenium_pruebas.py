from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = 'https://br.investing.com/currencies/usd-eur-historical-data'

browser.get(url)

title = browser.title

print(title)


cookies_accept_button = WebDriverWait(browser, 5).until( EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
cookies_accept_button.click()

calendar = browser.find_element(by=By.CLASS_NAME, value="DatePickerWrapper_icon-wrap__cwTu_")

calendar.click()


time.sleep(2)