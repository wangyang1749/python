from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://music.163.com/")
time.sleep(2)
html = driver.page_source
driver.close()
print(html)