#importacion de librerias
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Se declara variable para el driver y se localiza el path driver
driver=webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
#Se realiza la conexion a la pagina
driver.get("https://demoqa.com")
# se maximiza la pagina
driver.maximize_window()
#espera el tiempo definido para esperar a que localice los objetos
driver.implicitly_wait(10)

t=1

driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]").click()
time.sleep(t)
driver.find_element(By.XPATH,"//span[contains(text(),'Check Box')]").click()
time.sleep(t)
driver.find_element(By.XPATH,"//*[@id='tree-node']/ol/li/span/button").click()
time.sleep(t)

#Clcic en flechas desplegables
btn1=WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='tree-node']/ol/li/ol/li[1]/span/button")))
btn1.click()
time.sleep(t)
btn2=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='tree-node']/ol/li/ol/li[2]/span/button")))
btn2.click()
time.sleep(t)
btn3=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='tree-node']/ol/li/ol/li[3]/span/button")))
btn3.click()
time.sleep(t)
btn4=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='tree-node']/ol/li/ol/li[2]/ol/li[1]/span/button")))
btn4.click()
time.sleep(t)
btn5=WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='tree-node']/ol/li/ol/li[2]/ol/li[2]/span/button")))
btn5.click()
time.sleep(t)

#Seleccionar Checkbox
chk1=WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,"//span[@class='rct-title'][contains(.,'Angular')]")))
chk1.click()
time.sleep(t)
chk2=WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,"//span[@class='rct-title'][contains(.,'Private')]")))
chk2.click()
time.sleep(t)
chk3=WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,"//span[@class='rct-title'][contains(.,'Word File.doc')]")))
chk3.click()
time.sleep(t)
chk4=WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,"//span[@class='rct-title'][contains(.,'Notes')]")))
chk4.click()
time.sleep(t)

print(driver.title)
driver.close()

