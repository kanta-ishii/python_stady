from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.youtube.com/')
wait = WebDriverWait(driver, 10)

#continue処理する
element = wait.until(EC.title_contains("広告をスキップ"))
driver.find_element_by_link_text('広告をスキップ').click()
if input() == 'q':
    driver.quit()