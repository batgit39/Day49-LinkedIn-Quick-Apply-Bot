import time
from types import resolve_bases
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys 

EMAIL = ""
PASSWORD = ""
PHONE = ""
# fill your details

#setup selenium
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service('/home/mitresh/Development-Selenium/chromedriver'))
# enter your chromedriver location
driver.maximize_window()

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3590298959&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")

sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

time.sleep(2)

email_field = driver.find_element(By.ID, "username")
email_field.send_keys(EMAIL)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(5)
apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
apply_button.click()

#If application requires phone number and the field is empty, then fill in the number.
time.sleep(5)
phone = driver.find_element(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3590298959-6635267478496115791-phoneNumber-nationalNumber"]')
if phone.text == "":
    phone.send_keys(PHONE)

submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
submit_button.click()
time.sleep(5)
#Submit the application
while True:
    try:
        # submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
        button = driver.find_element(By.CLASS_NAME, "artdeco-button artdeco-button--2 artdeco-button--primary ember-view")
        button.click()
        print("good")
    except:
        print("wtf")
        break
    else:
        time.sleep(2)


