#Validar login completo
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

class ValidaLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
        self.driver.maximize_window()


    def test_login1(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        nom = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        psw = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        btn = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        nom.send_keys("AlexRdz")
        #time.sleep(3)
        psw.send_keys("admin123")
        #time.sleep(3)
        btn.click()
        error = driver.find_element(By.XPATH, "//h3[contains(@data-test,'error')]")
        error = error.text
        #print(error)
        if(error=="Epic sadface: Username and password do not match any user in this service"):
            print("Los datos no son correctos")
            print("Prueba 1 OK")
        time.sleep(3)

    def test_login2(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        nom = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        psw = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        btn = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        nom.send_keys("")
        #time.sleep(3)
        psw.send_keys("admin123")
        #time.sleep(3)
        btn.click()
        error = driver.find_element(By.XPATH, "//h3[@data-test='error'][contains(.,'Epic sadface: Username is required')]")
        error = error.text
        #print(error)
        if(error=="Epic sadface: Username is required"):
            print("Username requerido")
            print("Prueba 2 OK")
        time.sleep(3)

    def test_login3(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        nom = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        psw = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        btn = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        nom.send_keys("AlexRdz")
        # time.sleep(3)
        psw.send_keys("")
        # time.sleep(3)
        btn.click()
        error = driver.find_element(By.XPATH, "//h3[@data-test='error'][contains(.,'Epic sadface: Password is required')]")
        error = error.text
        #print(error)
        if (error == "Epic sadface: Password is required"):
            print("Password requerido")
            print("Prueba 3 OK")
        time.sleep(3)

    def test_loginCorrecto(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        nom = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        psw = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        btn = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")
        nom.send_keys("standard_user")
        # time.sleep(3)
        psw.send_keys("secret_sauce")
        # time.sleep(3)
        btn.click()
        titulo = driver.find_element(By.XPATH, "//div[contains(@class,'app_logo')]")
        titulo= titulo.text
        #print(titulo)
        if (titulo == "Swag Labs"):
            print("Login Correcto")
            print("Prueba 4 OK")
        time.sleep(3)

    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()
