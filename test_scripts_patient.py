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


       driver.get("https://durangopy-ebed-tracking-system.herokuapp.com/accounts/login/")
       time.sleep(2)
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user) # enter hardcoded username
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd) #enter hardcoded password
       elem = driver.find_element_by_xpath("/html/body/div/div/div/table/tbody/tr/td/form/p/input[1]")
       elem.send_keys(Keys.RETURN) # hit on enter
       time.sleep(4)
       elem = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/div/div/div/p/a[1]")
       elem.send_keys(Keys.RETURN)
       time.sleep(4)

       elem = driver.find_element_by_xpath("/html/body/div/div/div/div/a")
       elem.send_keys(Keys.RETURN)
       time.sleep(5)

       patient_tag = '89865'
       first_name = 'Deepthi'
       last_name = 'Akshay'
       cond = 'Non-serious'
       mode_of_arrival ='ambulance'
       age = '30'
       birth_date = '1988-08-20'
       phone_no = '4026128857'
       injuries = 'knee'
       deposition = 'none'
       time_of_surgery = '12:12:35'
       kin_name = 'Sandhya'
       relation ='cousin'


       elem = driver.find_element_by_id("id_patient_tag")
       elem.send_keys(patient_tag)
       elem = driver.find_element_by_id("id_first_name")
       elem.send_keys(first_name)
       elem = driver.find_element_by_id("id_last_name")
       elem.send_keys(last_name)
       elem = driver.find_element_by_xpath("/html/body/div/div/div/form/p[4]/select/option[3]").click()
       elem = driver.find_element_by_id("id_condition")
       elem.send_keys(cond)
       elem = driver.find_element_by_id("id_mode_of_arrival")
       elem.send_keys(mode_of_arrival)
       elem = driver.find_element_by_xpath("/html/body/div/div/div/form/p[8]/select/option[6]").click()
       elem = driver.find_element_by_id("id_age")
       elem.send_keys(age)
       elem = driver.find_element_by_id("id_birth_date")
       elem.send_keys(birth_date)
       elem = driver.find_element_by_id("id_phone")
       elem.send_keys(phone_no)
       elem = driver.find_element_by_id("id_injuries")
       elem.send_keys(injuries)
       elem = driver.find_element_by_id("id_deposition")
       elem.send_keys(deposition)
       elem = driver.find_element_by_id("id_time_of_surgery")
       elem.send_keys(time_of_surgery)
       elem = driver.find_element_by_id("id_kin_name")
       elem.send_keys(kin_name)
       elem = driver.find_element_by_id("id_relation")
       elem.send_keys(relation)
       time.sleep(2)
       elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button")
       elem.send_keys(Keys.RETURN)
       time.sleep(5)
       assert "success"

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()



