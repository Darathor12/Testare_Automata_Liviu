import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


class LoginPageObjects:
    USERNAME = "//input[@id='username']"
    PASSWORD = "//input[@id='password']"
    LOGIN_BUTTON = "//button[@id='submit']"
    LOGIN_SUCCESS_HEADER = "//h1[@class='post-title']"
    LOGOUT_BUTTON_LINK = "Log out"


class LoginPageData:
    LINK_LOGIN = "https://practicetestautomation.com/practice-test-login/"
    VALID_USERNAME = "student"
    VALID_PASSWORD = "Password123"
    LINK_VALID_LOGIN = "https://practicetestautomation.com/logged-in-successfully/"
    LOGIN_SUCCES_HEADER_TEXT = "Logged In Successfully"


class LoginTest(unittest.TestCase, LoginPageData, LoginPageObjects):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # self.driver.get(LoginPageData.LINK_LOGIN)
        self.driver.get(super().LINK_LOGIN) # daca vrei sa folosesti mostenire
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.wait_time = WebDriverWait(self.driver, 10)

    def tearDown(self) -> None:
        time.sleep(1)
        self.driver.quit()

    def test_login_success(self):
        # self.wait_time.until(EC.presence_of_element_located((By.XPATH, super().USERNAME)), "username field is not visible")
        self.wait_time.until(EC.presence_of_element_located((By.XPATH, super().USERNAME)), "username field not visible")
        username = self.driver.find_element(By.XPATH, super().USERNAME)
        username.send_keys(super().VALID_USERNAME)
        password = self.driver.find_element(By.XPATH, super().PASSWORD)
        password.send_keys(super().VALID_PASSWORD)
        time.sleep(1)

        self.wait_time.until(EC.element_to_be_clickable((By.XPATH, super().LOGIN_BUTTON)), "login button not visible")
        self.driver.find_element(By.XPATH, super().LOGIN_BUTTON).click()
        current_url = self.driver.current_url
        header_locator = self.driver.find_element(By.XPATH, super().LOGIN_SUCCESS_HEADER)
        logout_locator = self.driver.find_element(By.LINK_TEXT, super().LOGOUT_BUTTON_LINK)

        self.assertEqual(current_url, super().LINK_VALID_LOGIN, "Wrong link")
        self.assertEqual(header_locator.text, super().LOGIN_SUCCES_HEADER_TEXT, "Header Text not matching")
        assert logout_locator.is_displayed(), "Logout button is not displayed"





