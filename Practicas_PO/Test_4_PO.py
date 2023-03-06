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


tg = 1
class base_test2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")


    def test1(self):
        driver = self.driver
        f=Funciones_Globales(driver)
        f.Navegar("https://testpages.herokuapp.com/styled/file-upload-test.html", tg)
        f.Upload_ID("fileinput","C://Users//PRIDE OMEGA//Documents//Alex Rdz//Curso_Selenium//Curso_Selenium//Imagenes//Demo1.jpg", tg)
        f.Click_Xpath_Valida("//input[contains(@id,'itsanimage')]",tg)
        f.Click_Xpath_Valida("//input[contains(@value,'Upload')]", tg)
        f.Salida()


    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()