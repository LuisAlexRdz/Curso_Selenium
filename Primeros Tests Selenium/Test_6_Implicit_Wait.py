#importacion de librerias
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#Se declara variable para el driver y se localiza el path driver
driver=webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
#Se realiza la conexion a la pagina
driver.get("https://demoqa.com/text-box")
# se maximiza la pagina
driver.maximize_window()
#espera el tiempo definido pra esperar a que localice los objetos
driver.implicitly_wait(10)

#se declara variable para tiempo
t=.1
# se localizan los elementos
nom=driver.find_element(By.XPATH, "//*[@id='userName']")
nom.send_keys("Alex")
time.sleep(t)
driver.find_element(By.XPATH,"//input[contains(@id,'userEmail')]").send_keys("rdz.alex83@gmail.com")
time.sleep(t)
driver.find_element(By.XPATH,"//textarea[contains(@id,'currentAddress')]").send_keys("Direccion1")
time.sleep(t)
driver.find_element(By.XPATH,"//textarea[contains(@id,'permanentAddress')]").send_keys("Direccion2")
time.sleep(t)

#si se atravieza algun baner utilizar esta funcion
"""driver.execute_script("window.scrollto(0,300")
time.sleep(t)"""

driver.find_element(By.XPATH,value="//button[contains(@id,'submit')]").click()
time.sleep(t)

driver.close()