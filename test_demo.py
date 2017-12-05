import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
from Nurse_Patient_CRUD import *
from press_report import *
from TesScript_Hospital_CRUD import *
from TestScript_Nurselogin import *
from TestScript-ContactUs import *


class ConfigTestCase(unittest.TestCase):
    def setUp(self):
        print('set up')

    def runTest(self):
        print('run test')

# def suite():
#     # test_suite = unittest.TestSuite()
#
#
#     tc_1 = unittest.TestLoader().loadTestsFromTestCase(HomeTest_1)
#     # tc_2 = unittest.TestLoader().loadTestsFromTestCase(HomeTest_2)
#
#     # create a test suite combining search_text and home_page_test
#     test_suite = unittest.TestSuite([tc_1])
#
#     # test_suite.addTest(unittest.loader.findTestCases(tc1))
#     # test_suite.addTest(unittest.loader.findTestCases(tc2))
#
#     return test_suite
#
#
# mySuit = suite()
#
# runner = unittest.TextTestRunner()
# runner.run(mySuit)
#
# unittest.TextTestResult().run(mySuit)
