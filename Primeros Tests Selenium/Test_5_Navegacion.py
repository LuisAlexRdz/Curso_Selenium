import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="Drivers/chromedriver.exe")

t=2
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(t)

driver.get("https://www.google.com/webhp?hl=es-4t9&sa=X&ved=0ahUKEwiT3teslKr9AhVOlWoFHYaVDbgQPAgI")
time.sleep(t)

driver.get("https://test.igniite.io/auth")
time.sleep(t)

driver.execute_script("window.history.go(-1)")
time.sleep(t)
driver.execute_script("window.history.go(-1)")
time.sleep(t)
driver.execute_script("window.history.go(2)")
time.sleep(t)

driver.close()