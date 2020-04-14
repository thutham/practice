from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\Users\ACER\Downloads\chromedrive.exe")
driver.get("https://www.python.org")
print(driver.title)
