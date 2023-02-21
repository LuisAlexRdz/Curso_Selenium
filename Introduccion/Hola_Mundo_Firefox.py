from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

options=Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

driver=webdriver.Firefox(executable_path="Drivers/geckodriver.exe", options=options)

driver.get("https://demoqa.com/ text-box")

print(driver.title)

driver.close()
