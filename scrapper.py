from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
import time

# get input
username = ""
password = ""

# setup
options = Options()
options.headless = True
driver = webdriver.Firefox(options = options)
driver.get("https://www.instagram.com/")

# Check if cookies need to be accepted
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Decline optional cookies"]'))).click()
except NoSuchElementException:
    print("[Info] - Instagram did not require to accept cookies this time.")

# log in
username_form = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password_form = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
username_form.clear()
password_form.clear()
username_form.send_keys(username)
password_form.send_keys(password)
time.sleep(2) # crashes without this
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

# navigate to followers
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/" + username + "/?next=%2F']"))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/" + username + "/followers/?next=%2F']"))).click()

# scrape followers
time.sleep(5) # temporary fix, find a way for something to be clickable
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
followers_html = driver.find_elements(By.CLASS_NAME, "_aacl")
followers = []
for i in followers_html:
    followers.append(i.text)

for i in followers:
    print(i)

driver.close()