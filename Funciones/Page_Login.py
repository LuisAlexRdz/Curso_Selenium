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

class Pagina_Login():

    def __init__(self,driver):
        self.driver=driver

    def Login_Master(self,url,name,clave,t):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar(url,t)
        f.Texto_Xpath_Valida("//input[contains(@id,'user-name')]", name, t)
        f.Texto_Xpath_Valida("//input[contains(@id,'password')]", clave, t)
        f.Click_Xpath_Valida("//input[contains(@id,'login-button')]", t)
        f.Salida()
