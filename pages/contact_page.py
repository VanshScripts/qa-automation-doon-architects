from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class ContactPage:

    def __init__(self, driver):
        self.driver = driver

    # Fields
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    phone = (By.NAME, "phone")
    message = (By.NAME, "message")

    project_type = (By.NAME, "projectType")

    # Submit button
    submit = (By.XPATH, "//button[contains(.,'Send Enquiry')]")

    def fill_form(self, name, email, phone, message):
        self.driver.find_element(*self.name).send_keys(name)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.phone).send_keys(phone)
        self.driver.find_element(*self.message).send_keys(message)

    def select_project_type(self):
        dropdown = Select(self.driver.find_element(*self.project_type))
        dropdown.select_by_value("residential")  # matches your code

    def submit_form(self):
        button = self.driver.find_element(*self.submit)

        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)


        time.sleep(1.5)
        self.driver.execute_script("arguments[0].click();", button)