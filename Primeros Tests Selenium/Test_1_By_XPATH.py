import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="Drivers/chromedriver.exe")

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)

nom=driver.find_element(by=By.XPATH, value="//input[@type='text' and @id='userName']")
nom.send_keys("Alex")
time.sleep(2)
driver.find_element(By.XPATH,"//input[contains(@id,'userEmail')]").send_keys("rdz.alex83@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH,"//textarea[contains(@id,'currentAddress')]").send_keys("Direccion1")
time.sleep(1)
driver.find_element(By.XPATH,"//textarea[contains(@id,'permanentAddress')]").send_keys("Direccion2")
time.sleep(1)

#si se atravieza algun baner utilizar esta funcion
"""driver.execute_script("window.scrollto(0,300")
time.sleep(2)"""

driver.find_element(By.XPATH,value="//button[contains(@id,'submit')]").click()
time.sleep(2)
print(driver.title)

driver.close()