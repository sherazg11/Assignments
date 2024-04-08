from selenium import webdriver
from selenium.webdriver.common.by import By
import time
channels = []
n = int(input("How many channels you have? "))

for i in range(n):
    url = input()
    channels.append(url)


for url in channels:
    driver = webdriver.Chrome()
    driver.get(url)
    sub_button = driver.find_element(By.XPATH, "//button[@class='yt-spec-button-shape-next yt-spec-button-shape-next--filled yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m']")
    sub_button.click()
    time.sleep(10)
