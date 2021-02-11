import time
from selenium import webdriver
import chromedriver_binary

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
# driver.get('https://www.facebook.com/')
# driver.find_element_by_name('email').send_keys('konjiki.no.yami.234@gmail.com')
# driver.find_element_by_name('pass').send_keys('Wercome0')
driver.find_element_by_id('skip-button:39').click()



# ytp-ad-skip-button ytp-button