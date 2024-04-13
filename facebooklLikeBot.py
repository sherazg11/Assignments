from selenium import webdriver
from selenium.webdriver.common.by import By
import time
email_fb = "contact@peopleperhour.store"
pass_fb = "YomoLopo786"
user_id= "https://www.facebook.com/profile.php?id=61554043921157"
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

email_button = driver.find_element(By.ID, "email")
email_button.send_keys(email_fb)

pass_button = driver.find_element(By.ID, "pass")
pass_button.send_keys(pass_fb)

sub_button = driver.find_element(By.XPATH, "//button[@class='_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy']")
sub_button.click()

driver.execute_script("window.open('https://www.facebook.com/profile.php?id=61554043921157')")
driver.get(user_id)
like_button = driver.find_elements(By.XPATH, '//div[@aria-label="Like"]')
for like_button in like_button:
    like_button.click()
    print("Post Liked")

time.sleep(120)
