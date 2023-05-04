import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
from Funciones import Funciones_Globales
from Page_Login import Funciones_Login
from  selenium.webdriver import ActionChains
t= 1

@pytest.fixture(scope="module")
def setup_Login():
    global driver, f
    driver = webdriver.Chrome(executable_path='Drivers/chromedriver.exe')
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(20)
    f = Funciones_Globales(driver)
    f.Texto_Mixto("xpath", "//input[contains(@name,'username')]", "Admin", t)
    f.Texto_Mixto("xpath", "//input[contains(@type,'password')]", "admin123", t)
    f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Login')]", 3)
    print("Entrando al sistema")

def teardown_function():
    print("Fin del test")
    driver.close()

@pytest.mark.login
@pytest.mark.usefixtures("setup_Login")
def test_uno():
    etiqueta = f.SelElXp("//h6[contains(.,'Dashboard')]").text
    print(etiqueta)

    if (etiqueta=="Dashboart"):
        print("#####################\n")
        print("Estas en la pagina de inicio")
        print("\n#####################")
        assert  etiqueta== "Dashboard"
    else:
        assert etiqueta== "Dashboard" , "No pudiste entrar al sistema"
