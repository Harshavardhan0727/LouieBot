from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

def account_info():
    with open('account_info.txt', 'r') as f:
        info = f.read().split()
        email = info[0]
        password = info[1]
    return email, password

email, password = account_info()

tweet = 'hello, its louie'

options = Options()
options.add_argument("start.maximized")
driver = webdriver.chrome(options=options)

driver.get("https://twitter.com/login")