"""
from selenium import webdriver
import time

web = "https://www.instagram.com/eltallerdetd/"
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get(web)

seguidores = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')

followers = seguidores.text

print(followers)

driver.quit()
"""