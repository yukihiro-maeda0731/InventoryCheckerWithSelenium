from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()

# ログイン
driver.get("https://players.pokemon-card.com/login?redirect=/mypage")
formMailAddress = driver.find_element_by_id("formMailAddress")
formMailAddress.send_keys('ここにアドレス@gmail.com')
formPassword = driver.find_element_by_class_name("password")
formPassword.send_keys('ここにパスワード')
button = driver.find_elements_by_css_selector('.c-btn')
time.sleep(2)
button[2].click()

# イベントリンククリック
time.sleep(2)
eventLink = driver.find_elements_by_tag_name('a')
eventLink[4].click()

# キーワード入力
time.sleep(2)
eventName = driver.find_element_by_class_name("search")
eventName.send_keys('ルカリオHR争奪戦')

# 都道府県展開
time.sleep(2)
prefecture = driver.find_element_by_id("selectPrefectureText")
prefecture.click()

# 大阪にチェック
time.sleep(2)
driver.find_elements_by_class_name("c-checkbox")[31].click()

# 検索ボタン押下
time.sleep(2)
driver.find_element_by_css_selector('.p-searchForm-btn').click()
driver.find_elements_by_css_selector('.c-btn')[3].click()

