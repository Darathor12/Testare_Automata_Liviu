from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()     # numele 'driver' este cel mai intalnit
# se deschide automat o fila Chrome
sleep(2)

site_path = 'http://formy-project.herokuapp.com/form'
site_path_root = 'http://formy-project.herokuapp.com'
driver.get(site_path)
sleep(2)

# print(f'Title page: {driver.title}')
page_title = driver.title
print(f'Title page: {page_title}')

# driver.maximize_window()
# sleep(2)

# driver.minimize_window()
# sleep(2)
#
# driver.maximize_window()
# sleep(2)

# SELECTORI

# ----------------------------------------------------------------------------------
# Selector ID
driver.find_element(By.ID, "first-name").send_keys("MODIFICARE PRIN SELECTOR ID")
sleep(2)


elements = driver.find_elements(By.CLASS_NAME, "form-control")

# i = 0
# for element in elements:
#
#     print(f'{i}----|{element.text}|----')
#     if element.text:
#         pass
#     i += 1
# sleep(4)

# i = 0
# for element in elements:
#
#     print(f'{i}----|{element.id}|----')
#     if element.id == '0F9F1FD2294CBB73B8D06D700821E634_element_5':
#         element.send_keys('Vasilica')
#     i += 1
# sleep(4)

elemente_control = driver.find_elements(By.CLASS_NAME, 'form-control')
print(f'Avem {len(elemente_control)} elemente cu clasa form-control')
sleep(4)

# ----------------------------------------------------------------------------------
# Selector NAME
# Nu este unic
driver_root = webdriver.Chrome()
driver_root.get(site_path_root)
lista_elemente = driver_root.find_elements(By.TAG_NAME, 'a')
print(lista_elemente[17])

element_1 = lista_elemente[17]
element_1.click()
sleep(4)
