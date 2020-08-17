from selenium import webdriver
import unittest
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
import time

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://petstore.octoperf.com/actions/Catalog.action")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        print('Updated code for push')


    def test(self):
        driver = self.driver
        l = LoginPage(driver)
        l.login("xxxx", "yyyy")
        time.sleep(10)
        HomePage(driver).logout()
        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
