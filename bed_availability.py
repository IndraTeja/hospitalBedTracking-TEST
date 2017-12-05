import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class bed_availability(unittest.TestCase):

    def setUp(self):
       self.driver = webdriver.Chrome()

    def test_blog(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://durangopy-bed-track.herokuapp.com")
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div[1]/div/div/div/p/a")
        elem.click()

        def tearDown(self):
            self.driver.close()


if __name__ == "__main__":
    unittest.main()
