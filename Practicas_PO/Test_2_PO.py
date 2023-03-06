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
from Funciones.Page_Login import Pagina_Login

tg = 1
class base_test2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")


    def test1(self):
        driver = self.driver
        f= Funciones_Globales(driver)
        pg= Pagina_Login(driver)
        pg.Login_Master("https://www.saucedemo.com/", "AlexRdz", "Admin123", tg)
        f.Salida()



    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()