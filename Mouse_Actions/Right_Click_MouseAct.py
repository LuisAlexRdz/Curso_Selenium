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


t=2
class base_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
        #self.driver.maximize_window()


    def test1(self):
        driver = self.driver
        f= Funciones_Globales(driver)
        f.Navegar("https://demoqa.com/buttons",t)

        f.Mouse_Right_Click("id", "rightClickBtn")


    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()