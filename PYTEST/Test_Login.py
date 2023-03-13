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

t=.3
def test_login1():
    driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
    fl = Funciones_Login(driver)
    fl.L1("juan@yourstore.com","admin","No customer account found",t)
    fl.L2("","admin","Please enter your email",t)
    fl.L3("Alex","admin","Wrong email",t)
    fl.L4("admin@yourstore.com","","The credentials provided are incorrect",t)
    fl.L5("admin@yourstore.com","admin","Dashboard",t)

