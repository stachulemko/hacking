from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random


def register_and_check_email_availability(emails):
    driver = webdriver.Chrome()
    driver.get("https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=SignUp&ec=asw-gmail-globalnav-create&theme=glif")

    driver.find_element(By.NAME, 'firstName').send_keys("Imie")
    driver.find_element(By.NAME, "lastName").send_keys("Nazwisko")
    driver.find_element(By.CLASS_NAME, 'zQJV3').click()
    driver.find_element(By.NAME, 'day').send_keys("2")
    driver.find_element(By.ID, "month").send_keys("6")
    select_month = driver.find_element(By.NAME, "year", "1945")
    select_sex = driver.find_element(By.ID, "gender", "2")
    driver.find_element(By.CLASS_NAME, 'VfPpkd-vQzf8d').click()

    current_url1 = driver.current_url
    driver.find_element(By.CLASS_NAME, 'd3GVvd jGAaxb').click()
    driver.find_element(By.NAME, 'Username').send_keys(emails[0])
    driver.find_element(By.CLASS_NAME, 'VfPpkd-RLmnJb').click()
    current_url = driver.current_url


email_to_check = ["anna", "kowal", "dadasdfgfasfafda", "akepka"]
register_and_check_email_availability(email_to_check)

""" if current_url1 == current_url:
        print(f"istnieje {emails[0]}")
        for email in emails[1:]:
            print(f"wstawiamy: {email}")
            if current_url1 == current_url:
                print(f"istnieje {emails[email]}")
                driver.find_element(By.ID, "login").send_keys("")
                driver.find_element(By.ID, "login").clear()
                driver.find_element(By.ID, "login").send_keys(Keys.CONTROL + "a")
                driver.find_element(By.ID, "login").send_keys(Keys.DELETE)
            else:
                print(f"istnieje {emails[email]}")
                driver.get(current_url)
                driver.back()
                for email in emails[1:]:
                    print(f"wstawiamy: {email}")
                    if current_url1 == current_url:
                        print(f"istnieje {emails[email]}")
                        driver.find_element(By.ID, "login").send_keys("")
                        driver.find_element(By.ID, "login").clear()
                        driver.find_element(By.ID, "login").send_keys(Keys.CONTROL + "a")
                        driver.find_element(By.ID, "login").send_keys(Keys.DELETE)
                    else:
                        print(f"nie_istnieje {emails[email]}")
                        driver.get(current_url)
                        driver.back()
                        for email in emails[1:]:
                            print(f"wstawiamy: {email}")
                            if current_url1 == current_url:
                                print(f"istnieje {emails[email]}")
                                driver.find_element(By.ID, "login").send_keys("")
                                driver.find_element(By.ID, "login").clear()
                                driver.find_element(By.ID, "login").send_keys(Keys.CONTROL + "a")
                                driver.find_element(By.ID, "login").send_keys(Keys.DELETE)
                            else:
                                print(f"nie_istnieje {emails[email]}")
                                driver.get(current_url)
                                driver.back()
                                for email in emails[1:]:
                                    print(f"wstawiamy: {email}")
                                    if current_url1 == current_url:
                                        print(f"istnieje {emails[email]}")
                                        driver.find_element(By.ID, "login").send_keys("")
                                        driver.find_element(By.ID, "login").clear()
                                        driver.find_element(By.ID, "login").send_keys(Keys.CONTROL + "a")
                                        driver.find_element(By.ID, "login").send_keys(Keys.DELETE)
    else:
        print(f"nie_istnieje {emails[email]}")
        driver.get(current_url)
        driver.back()
        for email in emails[1:]:
            print(f"wstawiamy: {email}")
            if current_url1 == current_url:
                print(f"istnieje {emails[email]}")
                driver.find_element(By.ID, "login").send_keys("")
                driver.find_element(By.ID, "login").clear()
                driver.find_element(By.ID, "login").send_keys(Keys.CONTROL + "a")
                driver.find_element(By.ID, "login").send_keys(Keys.DELETE)

    time.sleep(8)
    x = driver.find_element(By.XPATH, "//div[@class='sc-bcXHqe ErrorContainer-sc-1hxvmp0-0 bHXXMt kAINnj NewEmailUserDataStep___StyledCustomErrorMessage-sc-nhf5cz-1 gfMenV']")
    print(x.tag_name)
    print(x.text)

    for email in emails[1:]:
        print(f"wstawiamy: {email}")
        driver.find_element(By.ID, "login").send_keys("")
        driver.find_element(By.ID, "login").clear()
        driver.find_element(By.ID, "login").send_keys(Keys.CONTROL + "a")
        driver.find_element(By.ID, "login").send_keys(Keys.DELETE)
        print(f'login:{driver.find_element(By.ID, "login").text}')
        time.sleep(random.randint(1, 3))
        driver.find_element(By.ID, "login").send_keys(email)
        time.sleep(1)
        x = driver.find_element(By.XPATH, "//div[@class='sc-bcXHqe ErrorContainer-sc-1hxvmp0-0 bHXXMt kAINnj NewEmailUserDataStep___StyledCustomErrorMessage-sc-nhf5cz-1 gfMenV']")
        print(x.text)

email_to_check = ["anna", "kowal", "dadasdfgfasfafda", "akepka"]
register_and_check_email_availability(email_to_check) """
