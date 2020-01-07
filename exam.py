# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class FINALEXAM1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\Ayush Arvind\\Desktop\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_f_i_n_a_l_e_x_a_m1(self):
        driver = self.driver
        driver.get(
            "https://media.prod.mdn.mozit.cloud/attachments/2012/07/09/3698/391aef19653595a663cc601c42a67116/image_upload_preview.html?myPhoto=7hgm3O1.jpg")
        driver.find_element_by_id("uploadImage").clear()
        um = driver.find_element_by_id("uploadImage")
        um.send_keys("E:\\Downloads\\P6240207.JPG")
        driver.save_screenshot("C:\\Users\\Ayush Arvind\\Desktop\\Successful Test.png")
        send = driver.find_element_by_xpath("//input[@value='Send']").click()

    def test_f_i_n_a_l_e_x_a_m2(self):
        driver = self.driver
        driver.get(
            "https://media.prod.mdn.mozit.cloud/attachments/2012/07/09/3698/391aef19653595a663cc601c42a67116/image_upload_preview.html?myPhoto=7hgm3O1.jpg")
        driver.find_element_by_id("uploadImage").clear()
        um = driver.find_element_by_id("uploadImage")
        um.send_keys("E:\\Downloads\\QAModule.pdf")
        try:um.send_keys("E:\\Downloads\\QAModule.pdf")
        except Exception as e:
            print(e)
            with self.assertRaises(UnexpectedAlertPresentException):
                um.send_keys("E:\\Downloads\\QAModule.pdf")
        driver.save_screenshot("C:\\Users\\Ayush Arvind\\Desktop\\Successful Test2.png")
        send = driver.find_element_by_xpath("//input[@value='Send']").click()

    def test_f_i_n_a_l_e_x_a_m3(self):
        driver = self.driver
        driver.get(
            "https://media.prod.mdn.mozit.cloud/attachments/2012/07/09/3698/391aef19653595a663cc601c42a67116/image_upload_preview.html?myPhoto=7hgm3O1.jpg")
        driver.find_element_by_id("uploadImage").clear()
        um = driver.find_element_by_id("uploadImage")
        um.send_keys("E:\\Downloads\\")
        driver.save_screenshot("C:\\Users\\Ayush Arvind\\Desktop\\Successful Test3.png")
        send = driver.find_element_by_xpath("//input[@value='Send']").click()


    def teardown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main(defaultTest="FINALEXAM1.test_f_i_n_a_l_e_x_a_m2")
