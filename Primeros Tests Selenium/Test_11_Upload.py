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
driver.get("https://testpages.herokuapp.com/styled/file-upload-test.html")
# se maximiza la pagina
driver.maximize_window()
#espera el tiempo definido para esperar a que localice los objetos
driver.implicitly_wait(10)

t=3

try:
    #Validar ComboBox
    buscar = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id,'fileinput')]")))
    buscar = driver.find_element(By.XPATH, "//input[contains(@id,'fileinput')]")
    buscar.send_keys("C://Users//DELL//OneDrive//Documentos//Alex Rdz//Curso_Selenium//Imagenes//Demo1.jpg")
    time.sleep(t)
    driver.find_element(By.XPATH, "//input[contains(@id,'itsanimage')]").click()
    driver.find_element(By.XPATH, "//input[contains(@value,'Upload')]").click()

except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")


time.sleep(t)
driver.close()

