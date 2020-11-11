import time
from selenium import webdriver
import secrets
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://webchartnow.com/bostonuniv/webchart.cgi')
user = driver.find_element_by_id('j_username')
password = driver.find_element_by_id('j_password')
user.send_keys(secrets.USERNAME)
password.send_keys(secrets.PASSWORD)
driver.find_element_by_class_name('input-submit').click()

# We are now logged in answer the survey
time.sleep(10)

btncontainer = driver.find_element_by_id('btn-container')
covid_buttons = btncontainer.find_elements_by_class_name('portal-btn-inner')
symptom_button = covid_buttons[1]
symptom_button.click()

time.sleep(5)
yes_button = driver.find_element_by_class_name('yes_btn')
yes_button.click()
time.sleep(3)

# Fill out phone number
phone_number_input = driver.find_elements_by_class_name("quest-userin")[0]
phone_number_input.send_keys(secrets.PHONE_NUMBER)

no_buttons = driver.find_elements_by_class_name('no_btn')

for button in no_buttons[1:]:
	button.click()

time.sleep(2)
driver.find_elements_by_class_name("form-save")[0].click()
