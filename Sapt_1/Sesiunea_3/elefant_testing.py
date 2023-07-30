import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



class ElefantTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://www.elefant.ro/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
        time.sleep(10)

    # - Test 1: Intrati pe site-ul https://www.elefant.ro/

    # metoda care se ruleaza la inceputul oricarui Test Case (scenariu de test)
    def test_open_site(self):
        time.sleep(2)

    # - Test 2: cautati un produs la alegere (iphone 14) si verificati ca s-au returnat cel putin 10 rezultate ([class="product-title"])
    def test_search_product(self):
        # search field
        search_field = self.driver.find_element(By.XPATH, "//input[@name='SearchTerm'][@class='form-control searchTerm js-has-overlay']")

        # send text to field
        search_field.send_keys("iphone 14")
        time.sleep(2)

        # click search button
        search_button = self.driver.find_element(By.XPATH, "//button[@class='btn-search btn btn-primary'][@name='search']")
        search_button.click()
        time.sleep(4)
        # extract products
        products = self.driver.find_elements(By.CLASS_NAME, "product-title")
        self.assertGreaterEqual(len(products), 10)

    # - Test 3: Extrageti din lista produsul cu pretul cel mai mic [@class="current-price "] (puteti sa va folositi de find_elements)
    def test_lowest_price_product(self):

        products = self.driver.find_elements(By.XPATH, "//div[@class='current-price ']")
        lowest_price = float("inf")

        for product in products:
            price_value = float(product.get_attribute("data-price"))
            if price_value < lowest_price:
                lowest_price = price_value

        print(f"Lowest current price is: {lowest_price}")

    # - Test 4: Extrageti titlul paginii si verificati ca este corect

    def test_title(self):
        print(f"Current title is: {self.driver.title.lower()}")
        self.assertIn("elefant", self.driver.title.lower())

    # - Test 5: Intrati pe site, accesati butonul cont si click pe conectare.
    # Identificati elementele de tip user si parola si inserati valori incorecte (valori incorecte inseamna oricare valori care nu sunt recunoscute drept cont valid)
    # - Dati click pe butonul "conectare" si verificati urmatoarele:
    #             1. Faptul ca nu s-a facut logarea in cont
    #             2. Faptul ca se returneaza eroarea corecta

    def test_login_failure(self):
        self.driver.find_element(By.XPATH, "//span[@class='login-prompt js-login-prompt']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[@class='my-account-login btn btn-primary btn-block']").click()
        time.sleep(1)
        username = self.driver.find_element(By.ID, "ShopLoginForm_Login")
        password = self.driver.find_element(By.ID, "ShopLoginForm_Password")
        username.send_keys("invalid@yahoo.com")
        time.sleep(1)
        password.send_keys("invalid")
        time.sleep(1)
        login_button = self.driver.find_element(By.NAME, "login")
        login_button.click()
        time.sleep(2)

        # message error label
        error_message = self.driver.find_element(By.XPATH, "//div[@role='alert']")
        self.assertTrue(error_message.is_displayed())

    # - Test 6: Stergeti valoarea de pe campul email si introduceti o valoare invalida (adica fara caracterul "@") si verificati faptul ca butonul "conectare" este dezactivat
    def test_disabled_button_login(self):

        self.driver.find_element(By.XPATH, "//span[@class='login-prompt js-login-prompt']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[@class='my-account-login btn btn-primary btn-block']").click()
        time.sleep(1)
        username = self.driver.find_element(By.ID, "ShopLoginForm_Login")
        password = self.driver.find_element(By.ID, "ShopLoginForm_Password")
        username.send_keys("invalid@yahoo.com")
        time.sleep(1)
        password.send_keys("invalid")
        time.sleep(1)
        login_button = self.driver.find_element(By.NAME, "login")
        login_button.click()
        time.sleep(3)

        username = self.driver.find_element(By.ID, "ShopLoginForm_Login")
        username.clear()
        time.sleep(1)
        username.send_keys("username_invalid")
        time.sleep(2)

        login_button = self.driver.find_element(By.NAME, "login")

        self.assertTrue(login_button.get_attribute("disabled"), "Button is not disabled")


    # metoda care se ruleaza la finalul fiecarui Test Case
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
