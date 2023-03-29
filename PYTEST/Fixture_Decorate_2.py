import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
from Funciones import Funciones_Globales
from Page_Login import Funciones_Login
from  selenium.webdriver import ActionChains
t=1
f=""
driver=""

@pytest.fixture(scope="module")
def setup_login_uno():
    global driver, f
    driver = webdriver.Chrome(executable_path='Drivers/chromedriver.exe')
    driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    driver.maximize_window()
    f = Funciones_Globales(driver)
    f.Texto_Mixto("id", "Email", "admin@yourstore.com", t)
    f.Texto_Mixto("id", "Password", "admin", t)
    f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", 5)
    print("Entrando al sistema")
    yield
    print("Saliendo del login uno")
    driver.close()


@pytest.fixture(scope="module")
def setup_login_dos():
    global driver, f
    driver = webdriver.Chrome(executable_path='Drivers/chromedriver.exe')
    driver.get("https://test.igniite.io/auth")
    driver.maximize_window()
    f = Funciones_Globales(driver)
    f.Texto_Mixto("id", "user", "LuisAlexRdz", t)
    f.Texto_Mixto("id", "password", "Alex1983", t)
    f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'LOG IN')]", 5)
    print("Entrando al sistema")
    yield
    print("Saliendo del login dos")
    driver.close()

@pytest.mark.usefixtures("setup_login_uno")
def test_uno():
    print("Entrando al sistema uno")

@pytest.mark.usefixtures("setup_login_dos")
def test_dos():
    print("Entrando al sistema dos")

