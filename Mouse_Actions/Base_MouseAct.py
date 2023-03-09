import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from Funciones.Funciones import Funciones_Globales
from  selenium.webdriver import ActionChains

t=2
class base_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
        #self.driver.maximize_window()


    def test1(self):
        driver = self.driver
        f= Funciones_Globales(driver)
        f.Navegar("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",t)
        f.Texto_Mixto("xpath","//input[@name='username']","Admin", t)
        f.Texto_Mixto("xpath","//input[@name='password']","admin123",t)
        f.Click_Mixto("xpath","//button[@type='submit']",t)
        f.Click_Mixto("xpath","//img[@src='/web/images/orangehrm-logo.png?1672659722816']",t)

        resource = driver.find_element(By.XPATH, "//a[@class='nav-link-hed'][contains(.,'Resources')]")
        subIn1 = driver.find_element(By.XPATH, "(//a[@href='orangehrm-resources/e-books/'])[1]")
        subIn2 = driver.find_element(By.XPATH, "(//a[@href='blog/'][contains(.,'Blog')])[1]")
        subIn3 = driver.find_element(By.XPATH, "(//li[@class='sub-menu-title menu-title-row pt-2 pb-2'])[11]")
        subIn4 = driver.find_element(By.XPATH, "(//a[contains(.,'The HR Dictionary')])[1]")
        ssubIn1 = driver.find_element(By.XPATH, "(//a[@data-lf-fd-inspected-xbp1oaewrnz7edvj='true'])[1]")
        ssunIn2 = driver.find_element(By.XPATH, "(//a[@data-lf-fd-inspected-xbp1oaewrnz7edvj='true'])[4]")

        action = ActionChains(driver)
        action.move_to_element(resource).move_to_element(subIn1).move_to_element(subIn2).move_to_element(subIn4).move_to_element(subIn3).click().perform()
        action.move_to_element(ssubIn1).move_to_element(ssunIn2).click().perform()
        time.sleep(t)

    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()