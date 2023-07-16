################ CSS Selectors
"""
simbolul * - selecteaza toate elementele
#idElement - selecteaza elementul cu id-ul "idElement"
.form-control - selecteaza toate elementele care au clasa form-control
col-sm-8col-sm-offset-2 - selecteaza toate elementele care au cele cele doua clase

input - selecteaza toate elementele de tip input
div input - selecteaza toate elemntele de tip input care se afla intr-un div
div>input - selecteaza toate elementele de tip input care au ca parinte un div

strong+input - selecteaza primul input care este dupa un element strong
strong~input - selecteaza toate elementele de tip input precedate de un element strong

input[class='value'] - selecteaza toate elementele de tip input care au atributul class egal cu valoarea 'value'
input[class~='form-control'] - selecteaza toate elementele tip input care au inceput cu 'value'

[id|='radio-button'] - selecteaza toate elementele ale caror id e egal sau incepe cu radio-button

div:nth-of-type(3) - nth-of-type gaseste copilul de pe pozitia specifica ( in cazul de fata ar fi 3 )
div:first-of-type - primul element de acest tip
div:last-of-type - ultimul element de acest tip
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()

LINK = "https://formy-project.herokuapp.com/form"

driver.get(LINK)

driver.find_element(By.CSS_SELECTOR, "a")


# CSS doar cu ID
driver.find_element(By.CSS_SELECTOR,"#first-name")

# CSS cu tag si cu ID
driver.find_element(By.CSS_SELECTOR, "input#first-name")

# CSS tag si cu ID
driver.find_element(By.CSS_SELECTOR, "input[id='first-name']")

# CSS cu tag si placeholder
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter first name']")

# CSS tag cu clasa si atributul id
driver.find_element(By.CSS_SELECTOR, "input.form-control[id='first-name']")

# CSS tag cu type = radio
driver.find_element(By.CSS_SELECTOR, "input[type='radio']")

# CSS tag cu clasa care contine o parte din valoarea data
driver.find_element(By.CSS_SELECTOR, "input[class='form-control']")

time.sleep(3)