import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Emergency_Track(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(chrome_options=options)


   def test_hospital(self):
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
       driver.get("https://durangopy-ebed-tracking-system.herokuapp.com/admin/")
       assert "Logged In"
       time.sleep(5)
       driver.get("https://durangopy-ebed-tracking-system.herokuapp.com/admin/eBedTrack/hospital/add/")
       time.sleep(3)

       # Entering details of New Hospital
       elem = driver.find_element_by_id("id_hospital_id")
       elem.send_keys("NSH") # Hospital Id is entered
       elem = driver.find_element_by_id("id_hospital_name")
       elem.send_keys("Nebraska Spine Hospital") # Hospital Name is entered
       elem = driver.find_element_by_id("id_address")
       elem.send_keys("6901 N 72nd St #20300, Omaha, NE 68122") # Hospital Address is entered
       elem = driver.find_element_by_id("id_phone_no")
       elem.send_keys("4025723000") # Hospital phone no is entered
       time.sleep(2)
       driver.save_screenshot("Hospital_Detail_New.png")
       elem = driver.find_element_by_xpath(".//*[@id='hospital_form']/div/div/input[1]").click() # Details are saved by clicking on save button
       time.sleep(5)
       driver.save_screenshot("Hospital_New.png")

       # Reading a Hospital Details
       time.sleep(3)
       driver.get("https://durangopy-ebed-tracking-system.herokuapp.com/admin/")
       time.sleep(2)
       elem = driver.find_element_by_xpath(".//*[@id='content-main']/div[2]/table/tbody/tr[4]/th/a").click() #Hospital is selected from Home screen
       elem = driver.find_element_by_xpath(".//*[@id='result_list']/tbody/tr/th/a").click() # Hospital is selected based on its Xpath to check the details of the hospital
       time.sleep(2)
       driver.save_screenshot("Hospital_Read.png")
       driver.back()
       time.sleep(2)

       # Updating a Hospital Details
       driver.get("https://durangopy-ebed-tracking-system.herokuapp.com/admin/")
       time.sleep(1)
       elem = driver.find_element_by_xpath(".//*[@id='content-main']/div[2]/table/tbody/tr[4]/th/a").click() #Hospital is selected from Home screen
       elem = driver.find_element_by_xpath(".//*[@id='result_list']/tbody/tr/th/a").click() # Hospital is selected based on its Xpath to check the details of the hospital.
       time.sleep(3)
       driver.save_screenshot("Hospital_Before_Update.png")
       time.sleep(3)
       elem = driver.find_element_by_id("id_hospital_id").clear()
       elem = driver.find_element_by_id("id_hospital_name").clear()
       time.sleep(3)
       elem = driver.find_element_by_id("id_hospital_id")
       elem.send_keys("SSH")
       elem = driver.find_element_by_id("id_hospital_name")
       elem.send_keys("Select Speciality Hospital")
       time.sleep(3)
       driver.save_screenshot("Hospital_After_Update.png")
       elem = driver.find_element_by_xpath(".//*[@id='hospital_form']/div/div/input[1]").click()
       time.sleep(3)
       driver.save_screenshot("Hospital_Updated.png")

       # Deleting a Hospital
       time.sleep(3)
       elem = driver.find_element_by_xpath(".//*[@id='result_list']/tbody/tr/td[1]/input").click() # Selecting the hospital based on Xpath
       elem = driver.find_element_by_xpath(".//*[@id='changelist-form']/div[1]/label/select").click() # Selecting the dropdown
       elem = driver.find_element_by_xpath(".//*[@id='changelist-form']/div[1]/label/select/option[2]").click() # Selecting the delete option in dropdown
       elem = driver.find_element_by_xpath(".//*[@id='changelist-form']/div[1]/button").click()
       time.sleep(3)
       elem = driver.find_element_by_xpath(".//*[@id='content']/form/div/input[4]").click() #Confirming to Delete the selected hospital
       time.sleep(3)
       driver.save_screenshot("Hospital_Delete.png")



       assert "Posted Hospital Entry"

   def tearDown(self):
       self.driver.close()


if __name__ == "__main__":
   unittest.main()
