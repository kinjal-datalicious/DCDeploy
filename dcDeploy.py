#!/usr/bin/env python
from selenium import webdriver
from time import sleep
from random import randint
import platform

platform_type = platform.system()
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--headless')

def driver_def():
    driver = None

    if platform_type == "Darwin":
        driver = webdriver.Chrome(
            executable_path="/Users/apple/.npm-global/bin/chromedriver",
            chrome_options=chromeOptions
        )
    if platform_type == "Linux":
        driver = webdriver.Chrome(
            executable_path="linux_chromeDriver/chromedriver",
            chrome_options=chromeOptions
        )
    return driver

for x in range (randint(0, 10)):
    driver = driver_def()
    driver.get("https://test.roibooster.com")
    driver.implicitly_wait(6)
    driver.set_window_size(1440,900)
    title = driver.title
    print title
    sleep(3)
    driver.quit()
