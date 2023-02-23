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
driver.get("https://www.globalsqa.com/angularjs-protractor-practice-site/")
# se maximiza la pagina
driver.maximize_window()
#espera el tiempo definido para esperar a que localice los objetos
driver.implicitly_wait(10)

t=3
#Ruta para practica
driver.find_element(By.XPATH,"//a[@href='/angularJs-protractor/SearchFilter']").click()
time.sleep(t)
"""driver.find_element(By.XPATH,"//input[@id='input1']").send_keys("InternetBill")
time.sleep(t)"""

try:
    #Validar ComboBox
    accountSelect=WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//select[contains(@id,'input2')]")))
    acc=Select(accountSelect)
    acc.select_by_index(2)
    time.sleep(t)
    acc.select_by_visible_text("All Accounts")
    time.sleep(t)
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")

typSelect=driver.find_element(By.XPATH, "//select[contains(@id,'input3')]")
ty=Select(typSelect)

ty.select_by_value("EXPENDITURE")
time.sleep(t)
ty.select_by_index(2)
time.sleep(t)

driver.close()

