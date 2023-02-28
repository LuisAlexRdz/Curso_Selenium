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
driver.get("https://formy-project.herokuapp.com/form")
# se maximiza la pagina
driver.maximize_window()
#espera el tiempo definido para esperar a que localice los objetos
driver.implicitly_wait(10)

t=3

links = driver.find_elements(By.TAG_NAME, ('a'))

print("El numero de links en la pagina es: ", len(links))

for num in links:
    print(num.text)

driver.find_element(By.LINK_TEXT, "Components").click()
time.sleep(t)
driver.find_element(By.LINK_TEXT, "Modal").click()
time.sleep(t)

time.sleep(t)
driver.close()

