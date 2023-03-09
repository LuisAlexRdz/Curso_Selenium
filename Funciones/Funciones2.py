import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

class Funciones_Globales2():

    def __init__(self,driver):
        self.driver=driver

    def Tiempo(self,tie):
        t = time.sleep(tie)
        return t

#Funcion Navega Pagina
    def Navegar(self, Url, tiempo):
        self.driver.get(Url)
        #self.driver.maximize_window()
        print("Pagina abierta: "+str(Url))
        t = time.sleep(tiempo)
        return t

#Funcion Valida Texto
    def Texto_Xpath_Valida(self, xpath, texto, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.clear()
            val.send_keys(texto)
            print("Escribiendo en el campo {} el texto {} ".format(xpath, texto))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento " + xpath)


    def Texto_ID_Valida(self, ID,texto,tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, ID)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self. driver.find_element(By.ID, ID)
            val.clear()
            val.send_keys(texto)
            print("Escribiendo en el campo {} el texto {} ".format(ID, texto))
            t = time.sleep(tiempo)
            return  t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento " + ID)


#Funcion Click
    def Salida(self):
        print("Se termina la prueba exitosamente")


    def Click_Xpath_Valida(self, xpath, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.click()
            print("Damos click en boton {} ".format(xpath))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento " + xpath)


    def Click_ID_Valida(self, ID, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, ID)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.ID, ID)
            val.click()
            print("Damos click en boton {} ".format(ID))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento " + ID)

