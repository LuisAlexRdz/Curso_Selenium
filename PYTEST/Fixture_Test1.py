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
f=""
driver=""

def setup_function(function):
    global driver,f
    driver = webdriver.Chrome(executable_path='Drivers/chromedriver.exe')
    driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    driver.maximize_window()
    f = Funciones_Globales(driver)
    f.Texto_Mixto("id", "Email", "admin@yourstore.com", t)
    f.Texto_Mixto("id", "Password", "admin", t)
    f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
    print("Iniciando los test")

def teardown_function(function):
    print("Fin de los test")
    driver.close()

def test_uno():
    f.Click_Mixto("xpath","//a[@href='#'][contains(.,'Catalog')]",t)
    f.Click_Mixto("xpath","(//i[contains(@class,'nav-icon far fa-dot-circle')])[1]",t)
    f.Texto_Mixto("id","SearchProductName","computer",t)
    f.Click_Mixto("id","search-products",5)

def test_dos():
    #f= Funciones_Globales
    f.Click_Mixto("xpath","//a[@href='#'][contains(.,'Catalog')]",t)
    f.Click_Mixto("xpath","(//i[contains(@class,'nav-icon far fa-dot-circle')])[1]",t)
    f.Click_Mixto("xpath","//a[@href='/Admin/Product/Create']",t)
    f.Texto_Mixto("xpath","//input[@id='Name']","Monitor",t)
    f.Texto_Mixto("xpath","//textarea[contains(@id,'ShortDescription')]","Monitor Philips 27",t)
    f.Click_Mixto("xpath","//span[@class='tox-mbtn__select-label'][contains(.,'File')]",t)
    f.Click_Mixto("xpath","//span[@class='tox-mbtn__select-label'][contains(.,'File')]",t)
    driver.switch_to.frame(0)
    #f.Texto_Mixto("xpath","//body", "Monitor Curvo 27 pulgadas, sin biseles, FHD 1920x1080, Game Mode, FreeSync, Eco Saving Plus, Flicker Free, 1x HDMI 1.4, 1x D-sub, 4ms(GTG), Dark Blue Gray (LC27R500FHLXZX)", t)
    campo=driver.find_element(By.XPATH,"//body")
    campo.send_keys("Monitor Curvo 27 pulgadas, sin biseles, FHD 1920x1080, Game Mode, FreeSync, Eco Saving Plus, Flicker Free, 1x HDMI 1.4, 1x D-sub, 4ms(GTG), Dark Blue Gray (LC27R500FHLXZX)"+ Keys.TAB+"MON_PHL")
    #f.Texto_Mixto("xpath","//input[contains(@id,'Sku')]","MON_PHL",t)







