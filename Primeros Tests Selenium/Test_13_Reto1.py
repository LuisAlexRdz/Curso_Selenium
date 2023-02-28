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
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
# se maximiza la pagina
driver.maximize_window()
#espera el tiempo definido para esperar a que localice los objetos
driver.implicitly_wait(10)

t=2

driver.find_element(By.XPATH,"//input[contains(@name,'firstname')]").send_keys("Alex" + Keys.TAB + "Rdz")
genero = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@value,'Male')]")))
genero.click()
years = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id,'exp-4')]")))
years.click()

driver.find_element(By.XPATH, "//input[contains(@id,'datepicker')]").send_keys("16/06/1983")
prof1 = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id,'profession-0')]")))
prof1.click()
prof2 = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id,'profession-1')]")))
prof2.click()

continentSelect = driver.find_element(By.XPATH, "//select[@id='continents']")
cont = Select(continentSelect)
ir = driver.execute_script("arguments[0].scrollIntoView();",continentSelect)
cont.select_by_index(4)

comandSelect = driver.find_element(By.XPATH, "//select[contains(@id,'selenium_commands')]")
comand = Select(comandSelect)
ir = driver.execute_script("arguments[0].scrollIntoView();",comandSelect)
comand.select_by_index(4)

try:
    #Validar ComboBox
    buscar = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id,'photo')]")))
    buscar = driver.find_element(By.XPATH, "//input[contains(@id,'photo')]")
    buscar.send_keys("C://Users//DELL//OneDrive//Documentos//Alex Rdz//Curso_Selenium//Imagenes//Demo1.jpg")
    ir = driver.execute_script("arguments[0].scrollIntoView();",buscar)
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")

driver.find_element(By.XPATH, "//button[contains(@id,'submit')]")

time.sleep(t)
driver.close()

