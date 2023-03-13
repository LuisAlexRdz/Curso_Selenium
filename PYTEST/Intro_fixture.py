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
from Page_Login import Funciones_Login
from  selenium.webdriver import ActionChains

t=1

def setup_function(function):
    print("Esto va al inicio de cada test")

def teardown_function(function):
    print("Esto va al final de cada test")


def test_uno():
    print("Test uno")

def test_dos():
    print("Test dos")

def test_tres():
    print("Test tres")