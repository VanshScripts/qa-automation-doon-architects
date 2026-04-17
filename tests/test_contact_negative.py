from selenium import webdriver
from pages.contact_page import ContactPage

def test_empty_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://doonarchitects.com/contact")

    contact = ContactPage(driver)

    contact.submit_form()

    assert "contact" in driver.current_url

    driver.quit()