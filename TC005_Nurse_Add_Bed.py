
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Blog_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       user = "unmc"
       pwd = "unmc2017"

       driver = self.driver
       driver.maximize_window()

       driver.get("https://durangopy-bed-track.herokuapp.com/")
       time.sleep(2)
       driver.get("https://durangopy-bed-track.herokuapp.com/accounts/login/")
       time.sleep(2)
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user) # enter hardcoded username
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd) #enter hardcoded password
       elem = driver.find_element_by_xpath("/html/body/div/div/div/table/tbody/tr/td/form/p/input[1]")
       elem.send_keys(Keys.RETURN) # hit on enter
       time.sleep(4)
       elem = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/p/a[2]")
       elem.send_keys(Keys.RETURN)
       time.sleep(4)

       elem = driver.find_element_by_xpath("/html/body/div/div/div/div[4]/a")
       elem.send_keys(Keys.RETURN)
       time.sleep(2)

       bed_id = "124"
       elem = driver.find_element_by_id("id_bed_id")
       elem.send_keys(bed_id)
       elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button")
       elem.send_keys(Keys.RETURN)
       time.sleep(3)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
