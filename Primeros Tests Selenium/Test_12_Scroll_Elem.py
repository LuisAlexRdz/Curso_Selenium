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
driver.get("https://pixabay.com/es/")
# se maximiza la pagina
driver.maximize_window()
#espera el tiempo definido para esperar a que localice los objetos
driver.implicitly_wait(10)

t=3

try:
    #Validar ComboBox
    buscar = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='label--Ngqjq'][contains(.,'Descubre más')]")))
    buscar = driver.find_element(By.XPATH, "//span[@class='label--Ngqjq'][contains(.,'Descubre más')]")
    ir = driver.execute_script("arguments[0].scrollIntoView();",buscar)
    time.sleep(t)

    #driver.execute_script("windows.scrollTo(0,800)")

except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")


time.sleep(t)
driver.close()

