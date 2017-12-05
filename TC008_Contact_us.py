import unittest
import time


from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TC008_Contact_us(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()




   def test_contact_us(self):
       driver = self.driver
       driver.maximize_window()
       driver.get("https://durangopy-bed-track.herokuapp.com/")
       assert "Logged In"

       # Click on Contact us tab-
       elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul/li[3]/a")
       elem.click()
       time.sleep(2)

      #To scroll down the page, executing script-
       driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

      # To contact hospital by Posting information
       elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/div/div/div/form/input[2]")
       elem.send_keys("Deepika")
       time.sleep(1)
       elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/div/div/div/form/input[3]")
       elem.send_keys("Jantz")
       time.sleep(1)
       elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/div/div/div/form/input[4]")
       elem.send_keys("djantz@unomaha.edu")
       time.sleep(1)
       elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/div/div/div/form/textarea")
       elem.send_keys("Kindly let me know if I can reserve an Emergency Situation -for my Sister In law who will be delivering in the next few days")
       time.sleep(1)

       elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/div/div/div/form/button")
       elem.click()
       time.sleep(2)






   def tearDown(self):
       self.driver.close()
