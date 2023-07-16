from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

# Selector NAME
# Nu este unic
site_path_root = 'http://formy-project.herokuapp.com'
driver_root = webdriver.Chrome()
driver_root.get(site_path_root)
lista_elemente = driver_root.find_elements(By.TAG_NAME, 'a')
print(lista_elemente[17])

element_1 = lista_elemente[17]
element_1.click()
sleep(4)

driver_root.back()
sleep(4)

# ------------------------------------------------------------------
# LINK TEXT
link_autocomplete = driver_root.find_element(By.LINK_TEXT, 'Autocomplete')
link_autocomplete.click()
sleep(2)

driver_root.back()
sleep(2)

# ------------------------------------------------------------------
# PARTIAL LINK TEXT
link_autocomp_partial = driver_root.find_element(By.PARTIAL_LINK_TEXT, 'Autocomp')
link_autocomp_partial.click()
sleep(2)
