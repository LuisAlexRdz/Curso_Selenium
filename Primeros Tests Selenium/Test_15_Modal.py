#importacion de librerias
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

#Se declara variable para el driver y se localiza el path driver
driver=webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
#Se realiza la conexion a la pagina
driver.get("https://formy-project.herokuapp.com/")
# se maximiza la pagina
driver.maximize_window()
#espera el tiempo definido para esperar a que localice los objetos
driver.implicitly_wait(10)

t=2

driver.find_element(By.XPATH, "//a[@class='btn btn-lg'][contains(.,'Modal')]").click()
driver.find_element(By.XPATH, "//button[contains(@id,'modal-button')]").click()
time.sleep(t)
try:
    #Validar ComboBox
    buscar=WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@id,'close-button')]")))
    buscar=driver.find_element(By.XPATH, "//button[contains(@id,'close-button')]").click()
    time.sleep(t)
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")

driver.find_element(By.XPATH, "//button[contains(@id,'modal-button')]").click()
time.sleep(t)
try:
    #Validar ComboBox
    buscar=WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@id,'ok-button')]")))
    buscar=driver.find_element(By.XPATH, "//button[contains(@id,'ok-button')]").click()
    time.sleep(t)
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")

time.sleep(t)
driver.close()

