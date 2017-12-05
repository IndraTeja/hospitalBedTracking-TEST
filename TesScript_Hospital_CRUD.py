#Author : Deepika
#Final Test Demo


import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class Test1_Hospital_CRUD(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_crud_hospital(self):
       user = "instructor"
       pwd = "instructor1a"

       driver = self.driver
       driver.maximize_window()


       driver.get("https://durangopy-bed-track.herokuapp.com/")
       elem=driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div[2]/a")
       elem.send_keys(Keys.RETURN)
       time.sleep(2)
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user) # enter hardcoded username
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd) #enter hardcoded password
       #Click on Login Button to login as an Admin
       elem = driver.find_element_by_xpath("/html/body/div/div/div/table/tbody/tr/td/form/p/input[1]")
       elem.send_keys(Keys.RETURN) # hit on enter
       time.sleep(2)
       #Click on View Hospital Information
       elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div/p/a[1]")
       elem.send_keys(Keys.RETURN)
       time.sleep(2)
       #Click on Add Hospital Button once you get to see the list of Hospitals
       elem = driver.find_element_by_xpath("/html/body/div/div/div/div/a")
       elem.send_keys(Keys.RETURN)
       time.sleep(2)

       Hospital_id = "chmc"
       Hospital_Name = "Creighton University Medical Center"
       Hospital_address = "5120 Charles St"
       Hospital_phone ="4026802537"

       elem = driver.find_element_by_id("id_hospital_id")
       elem.send_keys(Hospital_id)
       elem = driver.find_element_by_id("id_hospital_name")
       elem.send_keys(Hospital_Name)
       elem = driver.find_element_by_id("id_address")
       elem.send_keys(Hospital_address)
       elem = driver.find_element_by_id("id_phone_no")
       elem.send_keys(Hospital_phone)
        #Save the newly added form for Hospital
       elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button")
       elem.send_keys(Keys.RETURN)
       time.sleep(2)

       #To Edit a particular row
       elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/table/tbody/tr[5]/td[5]/a[1]")
       elem.send_keys(Keys.RETURN)
       time.sleep(2)

       #Change the hospital address in this case -
       elem = driver.find_element_by_id("id_address")
       elem.send_keys( "5120 Charles St, Omaha, NE 68132")

       # Click on Update Button-
       elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button")
       elem.send_keys(Keys.RETURN)
       time.sleep(2)

       #Click on Delete Button
       elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/table/tbody/tr[5]/td[5]/a[2]")
       elem.send_keys(Keys.RETURN)
       alertObj = driver.switch_to.alert
       alertObj.accept()

       time.sleep(2)

        #Click on OK button-




   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
