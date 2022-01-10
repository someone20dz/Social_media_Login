from selenium import webdriver
from time import sleep
from getpass import getpass

facebook_email = str(input("what's your Email/username: "))
facebook_password = getpass("what's your password:")

driver = webdriver.Chrome("Drivers/Chrome/chromedriver")
driver.get("http://www.facebook.com")

email_element = driver.find_element_by_id("email")
email_element.clear()
email_element.send_keys(facebook_email)

password_element = driver.find_element_by_id("pass")
password_element.clear()
password_element.send_keys(facebook_password)

Login_element = driver.find_element_by_name("login")
Login_element.click()