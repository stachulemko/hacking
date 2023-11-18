from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def register_and_check_email_availability(emails):
    driver = webdriver.Chrome()

    driver.get("https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=SignUp&ec=asw-gmail-globalnav-create&theme=glif")

    driver.find_element(By.NAME, 'firstName').send_keys("Imie")
    driver.find_element(By.NAME, "lastName").send_keys("Nazwisko")
    driver.find_element(By.CLASS_NAME, 'zQJV3').click()

    #driver.find_element(By.ID, "day").send_keys("23")
    driver.find_element(By.ID, "month").send_keys("6")
    select_month = driver.find_element(By.NAME, "year", "1945")
    select_sex = driver.find_element(By.ID, "gender", "2")
    driver.find_element(By.CLASS_NAME, 'VfPpkd-vQzf8d').click()

    for email in emails:
        driver.find_element(By.CLASS_NAME, 'd3GVvd.jGAaxb').click()
        username_field = driver.find_element(By.NAME, 'Username')
        username_field.send_keys(email)
        username_field.send_keys(Keys.RETURN)

        time.sleep(2)  # Wait for page transition or AJAX to complete

        current_url = driver.current_url
        if "Signup" in current_url:
            print(f"Email {email} is available")
            driver.back()
        else:
            print(f"Email {email} already exists")
            username_field.clear()
            driver.back()

    driver.quit()


email_to_check = ["anna", "kowal", "dadasdfgfasfafda", "akepka"]
register_and_check_email_availability(email_to_check)
