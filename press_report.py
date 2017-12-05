#Author : Indra Teja Chintakayala
#Final Test Demo


#modules
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Test5_press(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_1(self):
        # user = "instructor"
        # pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("https://durangopy-bed-track.herokuapp.com/")
        time.sleep(3)
        driver.get("https://durangopy-bed-track.herokuapp.com/press_report/")
        time.sleep(3)
        elem = driver.find_element_by_id("myInput")
        elem.send_keys("University")
        time.sleep(5)
        elem.clear()
        elem = driver.find_element_by_id("myInput")
        elem.send_keys("Children")
        time.sleep(5)
        elem.clear()
        elem = driver.find_element_by_id("myInput")
        elem.send_keys("Select")
        time.sleep(3)
        # assert "Logged In"
        # time.sleep(3)
        # elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[3]/table/tbody/tr[2]/th/a")
        # elem.click()
        # time.sleep(3)

    def tearDown(self):
                self.driver.close()

if __name__ == "__main__":
    unittest.main()