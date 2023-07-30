import time
import unittest
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestAlerts(TestCase):
    LINK = "https://the-internet.herokuapp.com/javascript_alerts"

    BUTTON_JS_ALERT_SIMPLE = (By.XPATH, "//button[@onclick='jsAlert()']")
    BUTTON_JS_ALERT_CONFIRM = (By.XPATH, "//button[@onclick='jsConfirm()']")
    BUTTON_JS_ALERT_PROMPT = (By.XPATH, "//button[contains(text(),'JS Prompt')]")

    P_RESULT = (By.ID, "result")

    # suprascriem metoda setUp care va rula inainte de fiecare test
    def setUp(self) -> None:
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get(self.LINK)
        time.sleep(1)

    # suprascriem metoda triedDown care va rula dupa fiecare test
    def tearDown(self) -> None:
        # time.sleep(3)
        self.driver.quit()

    # metoda ajutatoare - nu se ruleaza ca test
    # la fiecare click, self.click(self.NUME_LOCATOR)
    def click(self, locator):
        self.driver.find_element(*locator).click()

    def test_accept_simple_alert(self):
        self.click(self.BUTTON_JS_ALERT_SIMPLE)

        alert = self.driver.switch_to.alert

        alert.accept()

        expected_text = "You successfully clicked an alert"
        actual_text = self.driver.find_element(*self.P_RESULT).text

        self.assertEqual(expected_text, actual_text, "Error, text are not matching.")

    def test_cancel_confirm_alert(self):
        self.click(self.BUTTON_JS_ALERT_CONFIRM)

        alert = self.driver.switch_to.alert

        alert.dismiss()

        expected_text = "You clicked: Cancel"
        actual_text = self.driver.find_element(*self.P_RESULT).text

        self.assertEqual(expected_text, actual_text, "Error, text are not matching.")

    def test_accept_confirm_alert(self):
        self.click(self.BUTTON_JS_ALERT_CONFIRM)

        alert = self.driver.switch_to.alert

        alert.accept()

        expected_text = "You clicked: Ok"
        actual_text = self.driver.find_element(*self.P_RESULT).text

        self.assertEqual(expected_text, actual_text, "Error, text are not matching.")

    @unittest.skip
    def test_accept_prompt_alert_with_text(self):
        self.click(self.BUTTON_JS_ALERT_PROMPT)

        alert = self.driver.switch_to.alert
        alert.send_keys("test")
        alert.accept()

        expected_text = "You entered: test"
        actual_text = self.driver.find_element(*self.P_RESULT).text

        self.assertEqual(expected_text, actual_text, "Error, text are not matching.")

    @unittest.skip
    def test_cancel_prompt_alert_with_text(self):
        self.click(self.BUTTON_JS_ALERT_PROMPT)

        alert = self.driver.switch_to.alert
        alert.dismiss()

        expected_text = "You entered: null"
        actual_text = self.driver.find_element(*self.P_RESULT).text

        self.assertEqual(expected_text, actual_text, "Error, text are not matching.")

    @unittest.skip
    def test_accept_prompt_alert_without_text(self):
        self.click(self.BUTTON_JS_ALERT_PROMPT)

        alert = self.driver.switch_to.alert
        alert.accept()

        expected_text = "You entered:"
        actual_text = self.driver.find_element(*self.P_RESULT).text

        self.assertEqual(expected_text, actual_text, "Error, text are not matching.")