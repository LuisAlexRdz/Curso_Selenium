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
    def Texto_Mixto(self, tipo, selector, texto, tiempo):
        if (tipo=="xpath"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.XPATH, selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto {} ".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento " + selector)
                return t
        elif (tipo=="id"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.ID, selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto {} ".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento " + selector)


#Funcion Click
    def Click_Mixto(self, tipo,selector, tiempo):
        if (tipo == "xpath"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.XPATH, selector)
                val.click()
                print("Damos click en boton {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento " + selector)
        elif (tipo == "id"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.ID, selector)
                val.click()
                print("Damos click en boton {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento " + selector)

    def Salida(self):
        print("Se termina la prueba exitosamente")
