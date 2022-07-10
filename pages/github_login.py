import selenium
from driver.driver_chrome import driver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from decouple import config
import os

def login():
    login_user = driver.find_element(By.NAME, "login")
    login_pass = driver.find_element(By.NAME, "password")
    login_btn = driver.find_element(By.NAME, "commit")
    login_user.send_keys(config("USERNAME_GITHUB"))
    login_pass.send_keys(config("PASSWORD_GITHUB"))
    login_btn.click()
    