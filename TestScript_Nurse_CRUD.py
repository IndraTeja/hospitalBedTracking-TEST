import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Nurse_CRUD(unittest.TestCase):

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
       elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div/p/a[2]")
       elem.send_keys(Keys.RETURN)
       time.sleep(2)
       #Click on Add Hospital Button once you get to see the list of Hospitals
       elem = driver.find_element_by_xpath("/html/body/div/div/div/div/a")
       elem.send_keys(Keys.RETURN)
       time.sleep(2)

       Username = "chmc"
       password = "chmc2017"
       hospital_id = "/html/body/div/div/div/form/p[3]/select/option[2]"
       First_name ="Deepika"
       last_name = "Jantz"
       phone_no = "4021234541"

       elem = driver.find_element_by_id("id_username")
       elem.send_keys(Username)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(password)
       select = Select(driver.find_element_by_id("id_hospital_id"))
       select.select_by_visible_text('chmc')
       elem.click()
       elem = driver.find_element_by_id("id_first_name")
       elem.send_keys(First_name)
       elem = driver.find_element_by_id("id_last_name")
       elem.send_keys(last_name)
       elem = driver.find_element_by_id("id_phone_no")
       elem.send_keys(phone_no)
        #Save the newly added form for Hospital
       elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button")
       elem.send_keys(Keys.RETURN)
       time.sleep(2)

       #To Edit a particular row
       elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div/table/tbody/tr[3]/td[5]/a[1]")
       elem.send_keys(Keys.RETURN)
       time.sleep(2)

       #Change the Nurse First Name in this case -
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(password)
       elem = driver.find_element_by_id("id_first_name")
       elem.clear()
       elem.send_keys( "Deepika Angelene")

       # Click on Update Button-
       elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button")
       elem.send_keys(Keys.RETURN)
       time.sleep(2)

       #Click on Delete Button
       elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div/table/tbody/tr[3]/td[5]/a[2]")
       elem.send_keys(Keys.RETURN)
       alertObj = driver.switch_to.alert
       alertObj.accept()

       time.sleep(2)

        #Click on OK button-




   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()