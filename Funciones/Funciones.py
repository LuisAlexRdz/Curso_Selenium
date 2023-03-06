import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

class Funciones_Globales():

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
            return t

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
            return t

#Funcion Click
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
            return t

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
            return t

#Funcion Select
    def Select_Xpath_Type(self, xpath,tipo,dato, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val = Select(val)
            if (tipo=="text"):
                val.select_by_visible_text(dato)
            elif (tipo=="index"):
                val.select_by_index(dato)
            elif (tipo=="value"):
                val.select_by_value(dato)
            print("El texto seleccionado es {} ".format(dato))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento " + xpath)
            return t

    def Select_ID_Type(self, ID,tipo,dato, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, ID)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.ID, ID)
            val = Select(val)
            if (tipo=="text"):
                val.select_by_visible_text(dato)
            elif (tipo=="index"):
                val.select_by_index(dato)
            elif (tipo=="value"):
                val.select_by_value(dato)
            print("El texto seleccionado es {} ".format(dato))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento " + ID)
            return t

#Funcion Cargar Imagen
    def Upload_Xpath(self, xpath, ruta, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.send_keys(ruta)
            print("Se carga la imagen {} ".format(ruta))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro la imagen " + xpath)
            return t

    def Upload_ID(self, ID, ruta, tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, ID)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.ID, ID)
            val.send_keys(ruta)
            print("Se carga la imagen {} ".format(ruta))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro la imagen " + ID)
            return t

#Funcion Radio y Check
    def Check_Xpath(self, xpath,  tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.click()
            print("Se activa casilla checkbox {} ".format(xpath))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento " + xpath)
            return t

    def Check_ID(self, id,  tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.ID, id)
            val.click()
            print("Se activa casilla checkbox {} ".format(id))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento " + id)
            return t

    def Check_Xpath_Multiple(self, tiempo, *args):
        try:
            for num in args:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, num)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.XPATH, num)
                val.click()
                print("Se activa casilla checkbox {} ".format(num))
                t = time.sleep(tiempo)
                return t
        except TimeoutException as ex:
            for num in args:
                print(ex.msg)
                print("No se encontro el elemento " + num)


    def Salida(self):
        print("Se termina la prueba exitosamente")
