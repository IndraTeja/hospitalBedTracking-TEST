import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class view_details(unittest.TestCase):

    def setUp(self):
       self.driver = webdriver.Chrome()

    def test_blog(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://durangopy-ebed-tracking-system.herokuapp.com")
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/p/a")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[1]/td[3]/button")
        elem.click()
        time.sleep(2)

        def tearDown(self):
            self.driver.close()


if __name__ == "__main__":
    unittest.main()
