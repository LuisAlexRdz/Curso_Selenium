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
t=.5


@pytest.fixture(scope="module")
def setup_login_uno():
    print("Empezando el login del sistema uno")
    yield
    print("Saliendo del sistema uno prueba ok")

@pytest.fixture(scope="module")
def setup_login_dos():
    print("Empezando el login del sistema dos")
    yield
    print("Saliendo deñ sistema dos prueba ok")

def test_uno(setup_login_uno):
    print("##### Empezando las pruebas del test uno #####")

def test_dos(setup_login_dos):
    print("Esto es para la prueba dos")

@pytest.mark.usefixtures("setup_login_dos")
def test_tres():
    print("prueba tres")