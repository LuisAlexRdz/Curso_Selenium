#importacion de librerias
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

t=3

@pytest.fixture(scope="module")
def setup_inicio():
    global driver
    #Se declara variable para el driver y se localiza el path driver
    driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
    #Se realiza la conexion a la pagina
    driver.get("https://test.igniite.io/")
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://www.google.com/?client=ms-android-americamovil-mx-revc#sbfbu=0&pi=")
    # se maximiza la pagina
    driver.maximize_window()
    #espera el tiempo definido para esperar a que localice los objetos
    driver.implicitly_wait(5)

@pytest.mark.usefixtures("setup_inicio")
def test_uno():
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.XPATH,"//a[@class='gb_t'][contains(.,'Gmail')]").click()
    driver.find_element(By.XPATH,"/html/body/header/div/div/div/a[2]").click()
    driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys("rdz.alex83@gmail.com")
    driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span").click()
    driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input").send_keys("PEDROZA16061983")
    driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span").click()
    time.sleep(t)




@pytest.mark.usefixtures("setup_inicio")
def test_dos(setup_inicio):
    #Busca boton
    try:
        # Valida si existe boton y da click en boton get started
        buscar = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "(//button[@type='button'][contains(.,'GET STARTED')])[2]")))
        buscar = driver.find_element(By.XPATH, "(//button[@type='button'][contains(.,'GET STARTED')])[2]").click()
        time.sleep(t)
    except TimeoutException as ex:
        print(ex.msg)
        print("El elemento no esta disponible")
    # Da clic en opcion SIGN UP
    driver.find_element(By.XPATH,"//a[contains(.,'Sign up')]").click()
    time.sleep(t)
    # Valida que exita el nombre REGISTER
    pg_name = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div[2]/div[1]")
    name = pg_name.text
    print(name)

    if (name=='REGISTER'):
        driver.find_element(By.XPATH,"//input[@id='user']").send_keys("1892LuisAlex")
        driver.find_element(By.XPATH,"//input[contains(@id,'email')]").send_keys("rdz.alex83@gmail.com")
        driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Alex1983")
        driver.find_element(By.XPATH,"//input[contains(@id,'passwordConfirm')]").send_keys("Alex1983")
        driver.find_element(By.XPATH,"//input[@name='terms']").click()
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[3]/form/div[3]/div/div[1]/div/div[1]/div/span/button").click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/a/span").click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[2])
        #driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/div/div[2]/div[1]/div").click()
        time.sleep(10)
        #driver.find_element(By.XPATH,"")


    else:
        print("No se puede seguir con el registro")



