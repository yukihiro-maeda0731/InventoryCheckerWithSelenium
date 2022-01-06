from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.techwithtim.net/")
print(driver.title)

search = driver.find_element(by=By.NAME, value="s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
    main = element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"main"))
    )
    articles = main.find_elements(by=By.TAG_NAME, value="article")
    for article in articles:
        header = article.find_element(by=By.CLASS_NAME, value="entry-summary")
        print(header.text)
finally:
    driver.quit()

main = driver.find_element(by=By.ID, value="main")

driver.quit()