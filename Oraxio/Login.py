#importacion de librerias
import time
import pytest
import pyotp

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

t=3
key1 = pyotp.random_base32()
key = "NeuralNineMySuperSecretKey"
totp =pyotp.TOTP(key)
print(totp.now())


@pytest.fixture(scope="module")
def setup_login():
    global driver
    #Se declara variable para el driver y se localiza el path driver
    driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
    #Se realiza la conexion a la pagina
    driver.get("https://test.igniite.io/login")
    # se maximiza la pagina
    driver.maximize_window()
    # Se realiza el login a la pagina
    driver.find_element(By.XPATH,"//input[contains(@id,'user')]").send_keys("LuisAlexRdz")
    driver.find_element(By.XPATH,"//input[contains(@id,'password')]").send_keys("Alex1983")
    driver.find_element(By.XPATH,"//button[@type='submit'][contains(.,'LOGIN')]").click()
    time.sleep(t)
    #espera el tiempo definido para esperar a que localice los objetos
    driver.implicitly_wait(5)

@pytest.mark.usefixtures("setup_login")
def test_uno():
    print("Login correcto")
    time.sleep(t)






