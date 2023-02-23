import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="Drivers/chromedriver.exe")

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)

nom=driver.find_element(By.XPATH, "//input[@type='text' and @id='userName']")
nom.send_keys("Alex")
nom.send_keys(Keys.TAB + "rdz.alex83@gmail.com" + Keys.TAB + "Direccion1" + Keys.TAB + "Direccion2" + Keys.TAB + Keys.ENTER)
time.sleep(2)

driver.find_element(By.XPATH, "//span[@class='text'][contains(.,'Check Box')]").click()
time.sleep(2)

driver.close()