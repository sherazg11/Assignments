from selenium import webdriver
from selenium.webdriver.common.by import By
import time
channels = []

def login():
    print("Siging In Your Account")
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/")
    login_button = driver.find_element(By.XPATH, "//a[@class='yt-spec-button-shape-next yt-spec-button-shape-next--outline yt-spec-button-shape-next--call-to-action yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-leading']")
    login_button.click()
    driver.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&ec=65620&hl=en&ifkv=ARZ0qKLdcYUEk1Fo6LThzCn3CO0GvCcHa8ChkzCyBw0MRe5_SdZPKg-VzOnd_UtXA628jvIwC9v6&passive=true&service=youtube&uilel=3&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1123496035%3A1712595850193474&theme=mn&ddm=0")
    email_box = driver.find_element(By.XPATH, "//input[@class='whsOnd zHQkBf']")
    email_box.send_keys("asimbecker@gmail.com")
    next_button = driver.find_element(By.XPATH, "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b']")
    next_button.click()
    time.sleep(1500)
    pass_box = driver.find_element(By.XPATH, "//input[@type='password']")
    pass_box.send_keys("#Asimbecker11")
    next_button = driver.find_element(By.XPATH, "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b']")
    next_button.click()
    print("Signed In")
    time.sleep(1200)



def channel_count():
    n = int(input("How many channels you have? "))
    for i in range(n):
        url = input("Enter Url Of YT Channels: ")
        channels.append(url)

def susbcribers():
    for url in channels:
        driver = webdriver.Chrome()
        driver.get(url)
        sub_button = driver.find_element(By.XPATH, "//button[@class='yt-spec-button-shape-next yt-spec-button-shape-next--filled yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m']")
        sub_button.click()
        time.sleep(10)

channel_count()
login()
susbcribers()