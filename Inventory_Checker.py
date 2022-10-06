from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()

driver.get("https://players.pokemon-card.com/login?redirect=/mypage")
formMailAddress = driver.find_element_by_id("formMailAddress")
formMailAddress.send_keys('ここにアドレス@gmail.com')
formPassword = driver.find_element_by_class_name("password")
formPassword.send_keys('ここにパスワード')
button = driver.find_elements_by_css_selector('.c-btn')
time.sleep(2)
button[2].click()
time.sleep(1)
