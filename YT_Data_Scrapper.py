import json
from selenium import webdriver
from selenium.webdriver.common.by import By
list = []

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/playlist?list=PLbRlFdA6npILMecmm_5enuMcjasZRWMTr")
video_name_elements = driver.find_elements (By.XPATH, "//a[@id='video-title']")

for element in video_name_elements:
    video_name = element.text
    print ("Video Name: " , video_name)
    video = {"Video Name:": video_name}
    list.append(video)

file = open("yt.json", 'a')
file.write(json.dumps(list))
file.close()
