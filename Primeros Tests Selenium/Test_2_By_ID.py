import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="Drivers/chromedriver.exe")

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)

nom=driver.find_element(By.ID,"userName")
nom.send_keys("ALex")
time.sleep(2)
driver.find_element(By.ID,"userEmail").send_keys("rdz.alex83@gmail.com")
time.sleep(2)
driver.find_element(By.ID,value="currentAddress").send_keys("Direccion1")
time.sleep(1)
driver.find_element(By.ID,value="permanentAddress").send_keys("Direccion2")
time.sleep(1)

#si se atravieza algun baner utilizar esta funcion
"""driver.execute_script("window.scrollto(0,300")
time.sleep(2)"""

driver.find_element(By.ID,value="submit").click()
time.sleep(2)

driver.fi
driver.close()