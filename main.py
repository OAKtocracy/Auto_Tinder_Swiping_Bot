## AUTO TINDER SWIPPING BOT
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = 'C:/Users/name/Downloads/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('https://tinder.com/')


log_in = driver.find_element(By.LINK_TEXT, 'Log in')
time.sleep(5)
log_in.click()
time.sleep(5)

sign_in_with_fb = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button')
sign_in_with_fb.click()
time.sleep(5)

print(driver.window_handles)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
print(fb_login_window)
driver.switch_to.window(fb_login_window)
print(driver.title)

email_add = os.environ.get("email_addr")
pass_word = os.environ.get("pass")

email = driver.find_element(By.CSS_SELECTOR, '#email')
email.send_keys(email_add)

password = driver.find_element(By.CSS_SELECTOR, '#pass')
password.send_keys(pass_word)
password.send_keys(Keys.ENTER)
time.sleep(5)

driver.switch_to.window(base_window)
print(driver.title)
time.sleep(5)

allow = driver.find_element(By.CSS_SELECTOR, '#o1622039657 > main > div > div > div > div.Bgc\(\$c-ds-background-primary\).Py\(24px\).Px\(36px\) > button:nth-child(1) > div.w1u9t036 > div.l17p5q9z')
allow.click()
time.sleep(5)

not_interested_notification = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[2]/div[2]/div[2]')
not_interested_notification.click()
time.sleep(5)

i_accept_notification = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
i_accept_notification.click()
time.sleep(5)

driver.quit()
