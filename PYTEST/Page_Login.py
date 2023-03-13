import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
from Funciones import Funciones_Globales
from  selenium.webdriver import ActionChains

class Funciones_Login():

    def __init__(self,driver):
        self.driver=driver

    def L1(self,email,clave,message,t):
        driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
        f = Funciones_Globales(driver)
        f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)
        # driver.maximize_window()
        f.Texto_Mixto("xpath", "//input[contains(@id,'Email')]", email, t)
        f.Texto_Mixto("xpath", "//input[contains(@id,'Password')]", clave, t)
        f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
        e1 = f.SelElXp("//li[contains(.,'No customer account found')]")
        e1 = e1.text
        # print(e1)
        if (e1 == message):
            print("Prueba de validacion login incorrecto fue exitosa")
        else:
            print("Prueba no exitosa")
        driver.close()

    def L2(self,email,clave,message,t):
        driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
        '''options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        driver = webdriver.Firefox(executable_path="Drivers/geckodriver.exe", options=options)'''
        f = Funciones_Globales(driver)
        f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)
        # driver.maximize_window()
        f.Texto_Mixto("xpath", "//input[contains(@id,'Email')]", email, t)
        f.Texto_Mixto("xpath", "//input[contains(@id,'Password')]", clave, t)
        f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
        e1 = f.SelElXp("//span[contains(@id,'Email-error')]")
        e1 = e1.text
        if (e1 == message):
            print("Validacion campo Email es exitosa")
        else:
            print("Prueba no exitosa")
        driver.close()

    def L3(self,email,clave,message,t):
        driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
        f = Funciones_Globales(driver)
        f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)
        # driver.maximize_window()
        f.Texto_Mixto("xpath", "//input[contains(@id,'Email')]", email, t)
        f.Texto_Mixto("xpath", "//input[contains(@id,'Password')]", clave, t)
        f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
        e1 = f.SelElXp("//span[contains(@id,'Email-error')]")
        e1 = e1.text
        if (e1 == message):
            print("Validacion campo Email no valido es exitosa")
        else:
            print("Prueba no exitosaa")
        driver.close()

    def L4(self,email,clave,message,t):
        driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
        f = Funciones_Globales(driver)
        f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)
        # driver.maximize_window()
        f.Texto_Mixto("xpath", "//input[contains(@id,'Email')]", email, t)
        f.Texto_Mixto("xpath", "//input[contains(@id,'Password')]", clave, t)
        f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
        e1 = f.SelElXp("//li[contains(.,'The credentials provided are incorrect')]")
        e1 = e1.text
        # print(e1)
        if (e1 == message):
            print("Prueba de validacion password fue exitosa")
        else:
            print("Prueba no exitosa")
        driver.close()

    def L5(self,email,clave,message,t):
        driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
        f = Funciones_Globales(driver)
        f.Navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F", t)
        # driver.maximize_window()
        f.Texto_Mixto("xpath", "//input[contains(@id,'Email')]", email, t)
        f.Texto_Mixto("xpath", "//input[contains(@id,'Password')]", clave, t)
        f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
        m1 = f.SelElXp("//h1[contains(.,'Dashboard')]")
        m1 = m1.text
        if (m1 == message):
            print("Prueba de login fue exitosa")
        else:
            print("Prueba no exitosa")
        driver.close()
