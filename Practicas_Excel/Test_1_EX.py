import time
import unittest
from Funciones.Funciones_Excel import *

from selenium import webdriver
from Funciones.Funciones import Funciones_Globales
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

tg=.2

class base_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")

    def test1(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        fe = Funexcel(driver)
        f.Navegar("https://demoqa.com/text-box",tg)
        ruta = "C://Users//PRIDE OMEGA//Documents//Alex Rdz//Curso_Selenium//Curso_Selenium//Documentos//datos_ok.xlsx"
        filas = fe.getRowCount(ruta,"Hoja1")

        for i in range(2,filas+1):
            Nombre = fe.readData(ruta, "Hoja1", i , 1)
            Email = fe.readData(ruta, "Hoja1", i , 2)
            Direccion_uno = fe.readData(ruta, "Hoja1", i , 3)
            Direccion_dos = fe.readData(ruta, "Hoja1", i , 4)

            f.Texto_Mixto("xpath", "//input[contains(@id,'userName')]",Nombre, tg)
            f.Texto_Mixto("xpath", "//input[contains(@id,'userEmail')]", Email, tg)
            f.Texto_Mixto("xpath", "//textarea[contains(@id,'currentAddress')]", Direccion_uno, tg)
            f.Texto_Mixto("xpath", "//textarea[contains(@id,'permanentAddress')]", Direccion_dos, tg)
            f.Click_Xpath_Valida("//button[contains(@id,'submit')]", tg)

            e = f.Existe("id","name",tg)
            if (e == "Existe"):
                print("El elemento se inserto correctamente")
                fe.writeData(ruta,"Hoja1", i,5,"Insertado")
            else:
                print("No se inserto")
                fe.writeData(ruta, "Hoja1", i, 5, "Error")


    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()