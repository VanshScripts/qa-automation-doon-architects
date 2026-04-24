from selenium import webdriver
from pages.contact_page import ContactPage
import time

def test_contact_form():
    driver = webdriver.Chrome()
    driver.get("https://doonarchitects.com/contact")

    contact = ContactPage(driver)

    contact.fill_form(
        "Vansh",
        "test@gmail.com",
        "9876543210",  
        "Testing message"
    )

    contact.select_project_type()

    time.sleep(2) 

    contact.submit_form()

    driver.quit()