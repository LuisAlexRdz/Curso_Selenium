#importacion de librerias
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

t=3
#Se declara variable para el driver y se localiza el path driver https://nxtgenaiacademy.com/demo-site/
driver=webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
#Se realiza la conexion a la pagina
driver.get("https://accounts.lambdatest.com/register")
# se maximiza la pagina
driver.maximize_window()
#espera el tiempo definido para esperar a que localice los objetos
driver.implicitly_wait(10)

btn = driver.find_element(By.XPATH, "//button[contains(@data-testid,'signup-button')]")
btn.click()
full_name = driver.find_element(By.XPATH, "//p[@data-testid='errors-name'][contains(.,'Please enter your name')]")
name = full_name.text
#print("El valor del error es: " + name)

if (name=="Please enter your name"):
    #print("Falta el nombre")
    cn = driver.find_element(By.XPATH, "//input[contains(@data-testid,'name')]")
    cn.send_keys("Alex Rdz")
    time.sleep(t)

else:
    print("Nombre correcto")

ap_name = driver.find_element(By.XPATH, "//p[contains(@data-testid,'errors-email')]")
ap = ap_name.text
if (ap == "Please enter your email address"):
    # print("Falta el nombre")
    ap = driver.find_element(By.XPATH, "//input[contains(@id,'email')]")
    ap.send_keys("alex@gmail.com")
    time.sleep(t)
else:
    print("Apellido correcto")

print(btn.is_enabled())
if (btn.is_enabled()==False):
    print("Faltan campos por llenar")

time.sleep(t)
driver.close()

