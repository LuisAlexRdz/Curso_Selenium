import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from Funciones.Funciones2 import Funciones_Globales2
tg=1

class base_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")

    def test1(self):
        driver = self.driver
        f= Funciones_Globales2(driver)
        f.Navegar("https://demoqa.com/text-box", tg)
        f.Texto_Mixto("xpath", "//input[contains(@id,'userName')]", "Luis Alex Rdz", tg)
        f.Texto_Mixto("userEmail", "password", "Alex1983", tg)
        f.Texto_Mixto("xpath", "//textarea[contains(@id,'currentAddress')]", "Calle x #21", tg)
        f.Texto_Mixto("id", "permanentAddress", "Calle x #21", tg)
        f.Click_Mixto("xpath", "//button[contains(@id,'submit')]", tg)
        f.Salida()


    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()