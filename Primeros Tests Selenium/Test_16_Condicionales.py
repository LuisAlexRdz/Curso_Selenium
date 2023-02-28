#importacion de librerias
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

t=2
#Se declara variable para el driver y se localiza el path driver
driver=webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
#Se realiza la conexion a la pagina
driver.get("https://demoqa.com/")
# se maximiza la pagina
driver.maximize_window()
#espera el tiempo definido para esperar a que localice los objetos
driver.implicitly_wait(10)

titulo = driver.find_element(By.XPATH, "//img[@src='/images/Toolsqa.jpg']")
print(titulo.is_displayed())
bt1 = driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[1]/div[2]/div[1]/div[1]")

if (titulo.is_displayed()==True):
    print("Existe la imagen")
else:
    print("No existe la imagen")

time.sleep(t)
driver.close()

