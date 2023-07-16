from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()

LINK = "https://formy-project.herokuapp.com/form"

driver.get(LINK)

# Cauta primul element de tip input
driver.find_element(By.XPATH, "(//input)[1]")

# Cauta al doilea element de tip input
driver.find_element(By.XPATH, "(//input)[2]")

# Al doilea copil cu tag-ul <div> al unui element parinte oarecare - se observa ca parintele nu este specificat
driver.find_element(By.XPATH, "//div[2]")

# Al doilea copil cu tag-ul ORICARE * al unui element parinte oarecare, cu clasa 'form-control'
driver.find_element(By.XPATH, "//*[2][@class='form-control']")

# Primul element copil cu tag-ul <input> cu id='last-name' al unui parinte <div>
driver.find_element(By.XPATH, "//div/input[1][@id='last-name']")

# Ultimul element copil cu tag-ul <ption> al unui element parinte <select>
driver.find_element(By.XPATH, "//select/option[last()]")

# Penultimul element copil cu tag-ul <option> al unui element parinte <select>
driver.find_element(By.XPATH, "//select/option[last()-1]")

# Simbolul | (pipe) - se foloseste intre 2 XPATH-uri
# Simbolul | (pipe) - sau logic
# input cu id=id-inexistent sau input cu id=first-name
driver.find_element(By.XPATH, "//input[@id='id-inexistent'] | //input[@id='first-name']")

# Simbolul or - se foloseste intre 2 attribute
# Simbolul or - sau logic
# input cu id=first sau id=last
driver.find_element(By.XPATH, "//input[contains(@id,'first') or contains(@id,'last')]")

# Simbolul and - se foloseste intre 2 atribute
# Simbolul and - si logic
# input cu id=frist si id=name
driver.find_element(By.XPATH, "//input[contains(@id,'first') and contains(@id,'name')]")

# Simbol not - se foloseste la negarea atributului
# Simbol not - negare logica
driver.find_element(By.XPATH, "//input[not(@type='radio') and not(@type='checkbox')]")

#
# AXIS NAVIGATION
#
"""
ancestor           - selecteaza toti stramosii elementului din care pornim - IN SUS
ancestor-or-self   - selecteaza toti stramosii elementului din care pornim + elementul din care pornim - IN SUS
parent             - selecteaza STRICT parintele elementului din care pornim - IN SUS
descendent         - selecteze toti descendentii ( copiii, copiii copiilor ) elemtului din care pornim - IN JOS
descendent-of-self - selecteaza toti descendentii + elementul din care pornim - IN JOS
child              - selecteaza toti copiii nodului - IN JOS
following-sibling  - selecteaza fratii urmatorului element din care pornim - ACELASI NIVEL
precending-sibling - selecteaza fratii precedenti ai elementului din care pornim - ACELASI NIVEL
"""

# Stramosii <div> ai elementului label cu textul "First name"
driver.find_element(By.XPATH, "//label[text()='First name']/ancestor::div")

# TOTI stramosii elementului label cu textul "First name"
driver.find_element(By.XPATH, "//label[text()='First name']/ancestor::*")

# TOTI stramosii elementului label cu textul "First name" inclusiv <label>
driver.find_element(By.XPATH, "//label[text()='First name']/ancestor-or-self::*")

# Parintele elementului <label> cu textul="First name" cu tag specificat
driver.find_element(By.XPATH, "//label[text()='First name']/parent::strong")
driver.find_element(By.XPATH, "//label[text()='First name']/parent::*")

# Toti descendentii elemtului <div> avand clasa="input-group", indiferent de tip
driver.find_element(By.XPATH, "//div[@class='input-group']/descendant::*")
driver.find_element(By.XPATH, "//div[@class='input-group']/descendant::input")

# Toti descendentii elementului <div> avand clasa="input-group", indiferent de tip inclusiv cel din care pornim
driver.find_element(By.XPATH, "//div[@class='input-group']/descendant-or-self::*")

# Toti copiii elementului <div> cu clasa="input-group" care sunt si ei de tip <div>
driver.find_element(By.XPATH, "//div[@class='input-group']/child::div")

# Toti fratii dupa elementul <option> cu atributul value=2 care sunt si ei de tot de tip option
driver.find_element(By.XPATH, "//option[@value=2]/following-sibling::option")
driver.find_element(By.XPATH, "//option[@value=2]/following-sibling::*")

# Toti fratii inaintea elementul <option> cu atributul value=3 care sunt si ei de tot de tip option
driver.find_element(By.XPATH, "//option[@value=3]/preceding-sibling::option")
driver.find_element(By.XPATH, "//option[@value=3]/preceding-sibling::*")












