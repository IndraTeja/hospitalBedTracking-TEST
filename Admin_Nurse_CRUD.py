import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Emergency_Track(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(chrome_options=options)


   def test_nurse(self):
       user = "instructor"
       pwd = "instructor1a"
       driver = self.driver
       driver.maximize_window()
       driver.get("https://durangopy-ebed-tracking-system.herokuapp.com/admin")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       driver.get("https://durangopy-ebed-tracking-system.herokuapp.com/admin")
       assert "Logged In"
       time.sleep(5)
       driver.get("https://durangopy-ebed-tracking-system.herokuapp.com/admin/eBedTrack/nurse/add/")
       time.sleep(3)

       # Entering details of New Nurse
       elem = driver.find_element_by_id("id_first_name")
       elem.send_keys("Caren") # Nurse firstname is entered
       elem = driver.find_element_by_id("id_last_name")
       elem.send_keys("Mark") # Nurse lastname is entered
       elem = driver.find_element_by_id("id_address")
       elem.send_keys("6901 N 72nd St #20300, Omaha, NE 68122") # Nurse Address is entered
       elem = driver.find_element_by_id("id_phone_no")
       elem.send_keys("4025723000") # Nurse phone no is entered
       elem = driver.find_element_by_xpath(".//*[@id='id_hospital_id']").click()
       elem = driver.find_element_by_xpath(".//*[@id='id_hospital_id']/option[2]").click()
       time.sleep(1)
       elem = driver.find_element_by_xpath(".//*[@id='id_admin_id']").click()
       elem = driver.find_element_by_xpath(".//*[@id='id_admin_id']/option[2]").click()
       time.sleep(2)
       driver.save_screenshot("Nurse_Detail_New.png")
       elem = driver.find_element_by_xpath(".//*[@id='nurse_form']/div/div/input[1]").click() # Details are saved by clicking on save button
       time.sleep(5)
       driver.save_screenshot("Nurse_New.png")

       # Reading the Nurse Details
       time.sleep(3)
       driver.get("https://durangopy-ebed-tracking-system.herokuapp.com/admin/")
       time.sleep(2)
       elem = driver.find_element_by_xpath(".//*[@id='content-main']/div[2]/table/tbody/tr[5]/th/a").click() # Nurse is selected from Home screen
       elem = driver.find_element_by_xpath(".//*[@id='result_list']/tbody/tr/th/a").click() # Nurse is selected based on its Xpath to check the details of the hospital
       time.sleep(2)
       driver.save_screenshot("Nurse_Read.png")
       driver.back()
       time.sleep(2)

       # Updating the Nurse Details
       elem = driver.find_element_by_xpath(".//*[@id='result_list']/tbody/tr/th/a").click() # Nurse is selected based on its Xpath to check the details of the hospital.
       time.sleep(3)
       driver.save_screenshot("Nurse_Before_Update.png")
       time.sleep(3)
       elem = driver.find_element_by_id("id_first_name").clear()
       elem = driver.find_element_by_id("id_last_name").clear()
       elem = driver.find_element_by_id("id_address").clear()
       elem = driver.find_element_by_id("id_phone_no").clear()
       time.sleep(3)
       elem = driver.find_element_by_id("id_first_name")
       elem.send_keys("James")
       elem = driver.find_element_by_id("id_last_name")
       elem.send_keys("Ruck")
       elem = driver.find_element_by_id("id_address")
       elem.send_keys("145 S 94th Street Omaha")
       elem = driver.find_element_by_id("id_phone_no")
       elem.send_keys("4026664444")
       time.sleep(3)
       driver.save_screenshot("Nurse_After_Update.png")
       elem = driver.find_element_by_xpath(".//*[@id='nurse_form']/div/div/input[1]").click()
       time.sleep(3)
       driver.save_screenshot("Nurse_Updated.png")

       # Deleting a Nurse information
       time.sleep(3)
       elem = driver.find_element_by_xpath(".//*[@id='result_list']/tbody/tr/td[1]/input").click() # Selecting the Nurse based on Xpath
       elem = driver.find_element_by_xpath(".//*[@id='changelist-form']/div[1]/label/select").click() # Selecting the dropdown
       elem = driver.find_element_by_xpath(".//*[@id='changelist-form']/div[1]/label/select/option[2]").click() # Selecting the delete option in dropdown
       elem = driver.find_element_by_xpath(".//*[@id='changelist-form']/div[1]/button").click()
       time.sleep(3)
       elem = driver.find_element_by_xpath(".//*[@id='content']/form/div/input[4]").click() #Confirming to Delete the selected Nurse
       time.sleep(3)
       driver.save_screenshot("Nurse_Delete.png")



       assert "Posted Nurse Entry"

   def tearDown(self):
       self.driver.close()


if __name__ == "__main__":
   unittest.main()
