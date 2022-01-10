# Importing the webdriver abd Keys modules to provide all the required implementations
# Getpass Prompt the user for a password without echoing

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass

# Hello and Welcome
print("_________________                                             _________________")
print("                  Welcome to the Social-media Auto Login :) ")
print("_________________                                             _________________")
print("                    Which website you want to log in to? \n1.Facebook \n2.Insagram \n3.Twitter ")

# Select website
user_input = str(input("Choose a number: "))



# Saving account informations
if user_input == "1":

    def facebook_log():

        print("*****_______________ Facebook _______________*****")
        facebook_email = str(input("Enter your Email/username: "))
        print("The password is invisible but you still have to type it out")
        facebook_password = getpass('Enter your password:')

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome("Drivers/Chrome/chromedriver", options = options)
        driver.get("http://www.facebook.com")

        try:
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "_9vtf")))
        finally:
            email_element = driver.find_element_by_id("email")
            email_element.clear()
            email_element.send_keys(facebook_email)

            password_element = driver.find_element_by_id("pass")
            password_element.clear()
            password_element.send_keys(facebook_password)

            Login_element = driver.find_element_by_name("login")
            Login_element.click()

    facebook_log()
elif user_input == "2" or 3:
    print("Twitter and Instagram comming soon :D")
