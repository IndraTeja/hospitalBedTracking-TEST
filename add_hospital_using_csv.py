#Author : Indra Teja Chintakayala
#Assignment 4
#ISQA8210


#modules
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv


class Addhospital(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_hospital(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("https://durangopy-ebed-tracking-system.herokuapp.com/")
        time.sleep(3)
        driver.get("https://durangopy-ebed-tracking-system.herokuapp.com/admin/")
        time.sleep(3)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        assert "Logged In"
        time.sleep(3)

        with open('hospitals.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr[4]/th/a")
                elem.click()
                time.sleep(3)
                elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/ul/li/a")
                elem.click()
                elem = driver.find_element_by_id("id_hospital_id")
                elem.send_keys(line[0])
                time.sleep(2)
                elemt = driver.find_element_by_id("id_hospital_name")
                elemt.send_keys(line[1])
                time.sleep(2)
                elem = driver.find_element_by_id("id_address")
                elem.send_keys(line[2])
                time.sleep(2)
                elem = driver.find_element_by_id("id_phone_no")
                elem.send_keys(line[3])
                time.sleep(2)
                elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]")
                elem.click()
                driver.get("https://durangopy-ebed-tracking-system.herokuapp.com/admin/")

    def tearDown(self):
                self.driver.close()

if __name__ == "__main__":
    unittest.main()


