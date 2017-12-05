import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class Test3_Nurse_Patient_CRUD(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(chrome_options=options)


   def test_nurse(self):
       user = "unmc"
       pwd = "unmc2017"
       driver = self.driver
       driver.maximize_window()
       driver.get("https://durangopy-bed-track.herokuapp.com")
       elem = driver.find_element_by_xpath(".//*[@id='app-layout']/div[1]/div/div/div[2]/div/div/div/div[2]/a").click()
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       #driver.get("https://durangopy-bed-track.herokuapp.com/accounts/login")
       assert "Logged In"
       time.sleep(5)
       driver.get("https://durangopy-bed-track.herokuapp.com/accounts/profile")
       time.sleep(3)
       elem = driver.find_element_by_xpath(".//*[@id='app-layout']/div[1]/div/div/div[2]/div/div/div/div/div/p/a[1]").click()
       time.sleep(1)

       #Add Patient
       elem = driver.find_element_by_xpath(".//*[@id='app-layout']/div[1]/div/div/div/a/span").click()
       time.sleep(1)
       elem = driver.find_element_by_id("id_patient_tag").clear()
       time.sleep(2)
       elem = driver.find_element_by_id("id_patient_tag").send_keys("BMMC0008")
       elem = driver.find_element_by_id("id_bed_id")
       elem.send_keys(401)
       time.sleep(2)
       elem = driver.find_element_by_xpath(".//*[@id='id_condition']").click()
       elem = driver.find_element_by_xpath(".//*[@id='id_condition']/option[3]").click()
       elem = driver.find_element_by_xpath(".//*[@id='id_bed_type']").click()
       elem = driver.find_element_by_xpath(".//*[@id='id_bed_type']/option[5]").click()
       elem = driver.find_element_by_xpath(".//*[@id='id_patient_status']").click()
       time.sleep(5)
       elem = driver.find_element_by_xpath(".//*[@id='app-layout']/div[1]/div/div/form/button").click()

       #Reading the Patient Details
       driver.get("https://durangopy-bed-track.herokuapp.com/accounts/profile")
       time.sleep(3)
       elem = driver.find_element_by_xpath(".//*[@id='app-layout']/div[1]/div/div/div[2]/div/div/div/div/div/p/a[1]").click()
       time.sleep(1)
       elem = driver.find_element_by_xpath(".//*[@id='app-layout']/div[1]/div/div/div/div/table/tbody/tr[1]/td[8]/a").click()
       time.sleep(2)
       driver.get("https://durangopy-bed-track.herokuapp.com/patient")
       time.sleep(2)

       #Update the Patient Details
       #elem = driver.find_element_by_xpath(".//*[@id='app-layout']/div[1]/div/div/div[2]/div/div/div/div/div/p/a[1]").click()
       time.sleep(2)
       elem = driver.find_element_by_xpath(".//*[@id='app-layout']/div[1]/div/div/div/div/table/tbody/tr[1]/td[8]/a").click()
       elem = driver.find_element_by_id("id_first_name")
       elem.send_keys("Roki")
       time.sleep(2)
       elem = driver.find_element_by_id("id_last_name")
       elem.send_keys("Bramani")
       time.sleep(2)
       elem = driver.find_element_by_xpath(".//*[@id='app-layout']/div[1]/div/div/form/button").click()
       time.sleep(2)

       #Delete the Patient Details
       elem = driver.find_element_by_xpath(".//*[@id='app-layout']/div[1]/div/div/div/div/table/tbody/tr/td[9]/a").click()
       time.sleep(2)
       alertObj = driver.switch_to.alert
       alertObj.accept()
       time.sleep(2)








       #assert "Posted Nurse Entry"

   def tearDown(self):
       self.driver.close()


if __name__ == "__main__":
   unittest.main()