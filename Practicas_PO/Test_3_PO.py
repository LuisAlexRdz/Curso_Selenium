import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from Funciones.Funciones import Funciones_Globales


tg = 2
class base_test2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")


    def test1(self):
        driver = self.driver
        f= Funciones_Globales(driver)
        f.Navegar("https://www.globalsqa.com/angularJs-protractor/SearchFilter/", tg)
        f.Select_ID_Type("input2","index", "2", tg)
        #f.Select_Xpath_Text("//select[contains(@id,'input3')]", "INCOME", tg)
        f.Select_Xpath_Type("//select[contains(@id,'input3')]", "value", "INCOME", tg)
        f.Salida()




    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()