from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome()

LINK = "https://orteil.dashnet.org/cookieclicker/"

driver.get(LINK)

time.sleep(3)

cookie = driver.find_element(By.ID, "bigCookie")
cookie_count = driver.find_element(By.ID, "cookies")
item = driver.find_element(By.CSS_SELECTOR, "#productPrice0")

for i in range(5000):
    time.sleep(0.1)
    cookie.click()
    count = int(cookie_count.text.split(" ")[0])
    value = int(item.text)
    if value <= count:
        upgrade_actions = ActionChains(driver)
        upgrade_actions.move_to_element(item)
        upgrade_actions.click()
        upgrade_actions.perform()
