###Ruta server allure: http://192.168.137.1:50881/index.html###
###Ejecutar test: pytest .\Fixture_Decorate_2.py --alluredir="./allurereports"###
###abrir reporte: allure serve .\allurereports\

import time

import allure
import pytest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from  allure_commons.types import AttachmentType
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
f=""
driver=""

@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="Error", attachment_type=AttachmentType.PNG)

@pytest.fixture(scope="module")
def setup_login_uno():
    global driver, f
    driver = webdriver.Chrome(executable_path='Drivers/chromedriver.exe')
    driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    driver.maximize_window()
    driver.implicitly_wait(20)
    f = Funciones_Globales(driver)
    f.Texto_Mixto("id", "Email", "admin@yourstore.com", t)
    f.Texto_Mixto("id", "Password", "admin", t)
    f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'Log in')]", 3)
    print("Entrando al sistema")
    ##yield
    ##print("Saliendo del login uno")
    ##driver.close()


@pytest.fixture(scope="module")
def setup_login_dos():
    global driver, f
    ##driver.implicitly_wait(20)
    driver = webdriver.Chrome(executable_path='Drivers/chromedriver.exe')
    driver.get("https://test.igniite.io/")
    ##driver.maximize_window()
    f = Funciones_Globales(driver)
    allure.attach(driver.get_screenshot_as_png(), name="oraxio", attachment_type=AttachmentType.PNG)
    f.Click_Mixto("xpath","(//button[contains(.,'GET STARTED')])[2]",t)
    allure.attach(driver.get_screenshot_as_png(), name="login", attachment_type=AttachmentType.PNG)
    f.Texto_Mixto("id", "user", "LuisAlexRdz", t)
    allure.attach(driver.get_screenshot_as_png(), name="user", attachment_type=AttachmentType.PNG)
    f.Texto_Mixto("id", "password", "Alex1983", t)
    allure.attach(driver.get_screenshot_as_png(), name="psw", attachment_type=AttachmentType.PNG)
    f.Click_Mixto("xpath", "//button[@type='submit'][contains(.,'LOGIN')]", 3)
    print("Entrando al sistema")
    ##yield
    ##print("Saliendo del login dos")
    ##driver.close()

@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_login_uno")
def test_uno():
    print("Entrando al sistema uno")
    f.Click_Mixto("xpath","(//p[contains(.,'Customers')])[1]",t)
    f.Click_Mixto("xpath","(//p[contains(.,'Customers')])[2]",t)
    f.Click_Mixto("xpath","//i[contains(@class,'fas fa-plus-square')]",3)
    email=driver.find_element(By.ID,"Email")
    email.send_keys("alex2@mail.com"+Keys.TAB+"Alex123"+Keys.TAB+"Alex2"+Keys.TAB+"Rdz2")
    time.sleep(2)
    f.Check_Xpath("//input[@id='Gender_Male']",t)
    f.Texto_Mixto("xpath","//input[contains(@id,'DateOfBirth')]","6/16/1983",t)
    f.Texto_Mixto("id","Company","Hexaware",t)
    f.Check_ID("IsTaxExempt",t)
    f.Click_Mixto("xpath","(//div[@role='listbox'])[1]",t)
    f.Click_Mixto("xpath","//li[contains(.,'Your store name')]",t)
    f.Click_Mixto("xpath", "//input[contains(@aria-describedby,'SelectedCustomerRoleIds_taglist')]", t)
    f.Click_Mixto("xpath", "//li[contains(.,'Administrators')]", t)
    f.Click_Mixto("xpath","(//span[contains(@title,'delete')])[2]",t)
    f.Click_Mixto("xpath", "//input[contains(@aria-describedby,'SelectedCustomerRoleIds_taglist')]", t)
    f.Click_Mixto("xpath", "//li[@id='53a79c5a-e428-48d4-9c8a-8a87491e526e']", t)
    f.Select_Xpath_Type("//select[@id='VendorId']","index","2",t)
    f.Texto_Mixto("xpath","//textarea[@id='AdminComment']","Texto Largo",2)
    f.Click_Mixto("xpath","//textarea[@id='AdminComment']",3)


@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.usefixtures("setup_login_dos")
def test_dos():
    print("Entrando al sistema dos")
    f.Click_Mixto("xpath","//span[contains(.,'LIVE TRADING')]",t)
    allure.attach(driver.get_screenshot_as_png(),name="LIVE_TRADING",attachment_type=AttachmentType.PNG)
    f.Click_Mixto("xpath","//span[contains(.,'ACCOUNTS')]",t)
    allure.attach(driver.get_screenshot_as_png(), name="ACCOUNTS", attachment_type=AttachmentType.PNG)
    f.Click_Mixto("xpath","(//span[contains(.,'ADMIN')])[1]",t)
    allure.attach(driver.get_screenshot_as_png(), name="ADMIN", attachment_type=AttachmentType.PNG)
    f.Click_Mixto("xpath","//span[contains(.,'HOME')]",t)
    allure.attach(driver.get_screenshot_as_png(), name="HOME", attachment_type=AttachmentType.PNG)
    time.sleep(5)


def teardown_function():
    print("Salida del test")
    driver.close()
