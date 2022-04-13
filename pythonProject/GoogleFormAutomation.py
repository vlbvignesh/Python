from selenium import webdriver

# For using sleep function because selenium
# works only when the all the elements of the
# page is loaded.
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Creating an instance webdriver
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome(executable_path="C:\Program Files\ChromeDriver\chromedriver.exe")
browser.maximize_window()
browser.get('https://www.irctc.co.in/nget/train-search')

# Let's the user see and also load the element
time.sleep(2)

#login = browser.find_elements_by_xpath('//*[@id="doc"]/div[1]/div/div[1]/div[2]/a[3]')

# using the click function which is similar to a click in the mouse.
#login[0].click()

print("Login in Twitter")

Login = browser.find_elements_by_xpath('//html/body/app-root/app-home/div[1]/app-header/div[2]/div[2]/div[1]/a[1]')

# Enter User Name
Login[0].click()

time.sleep(2)

user = browser.find_elements_by_xpath('//*[@id="8251726"]')
user.send_keys('waste')
# Reads password from a text file because
# saving the password in a script is just silly.

Password = "test"
search = Select(user)
search.select_by_index(1)
#user.click()

LOG = browser.find_elements_by_xpath('//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/input[1]')
LOG[0].click()
print("Login Successful")
time.sleep(5)

elem = browser.find_element_by_name("q")
elem.click()
elem.clear()

elem.send_keys("Geeks for geeks ")

# using keys to send special KEYS
elem.send_keys(Keys.RETURN)

print("Search Successful")

# closing the browser
browser.close()
