from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.techwithtim.net/")
print(driver.title)

search = driver.find_element_by_name("s")
search.send_keys("seleniumにより自動入力")
search.send_keys(Keys.RETURN)

print(driver.page_source)

time.sleep(5)

driver.quit()