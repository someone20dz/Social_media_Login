from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass

print("----------------- Facebook Auto Login :)   -----------------")
print("Select an option: \n1.Log in with new data \n2.Login with existing data")

save_data = input("Save data to a file (Y/N) ?")

user_choice = input("Choose a number: ")
# save_data = input("Would you like to save this informations in a file (Y/N)? ")

def facebook_log():

    print("*****----------------- Facebook -----------------*****")
    facebook_email = str(input("Enter your Email/username: "))
    print("The password is invisible but you still have to type it ")
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

if user_choice == "1":
        facebook_log()
elif user_choice == "2":
    print("Comming soon")
