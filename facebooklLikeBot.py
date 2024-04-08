from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

email_button = driver.find_element(By.ID, "email")
email_button.send_keys("ahmadali@gmail.com")

pass_button = driver.find_element(By.ID, "pass")
pass_button.send_keys("ahmadali@gmail.com")

sub_button = driver.find_element(By.XPATH, "//button[@class='_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy']")
sub_button.click()

time.sleep(120)
