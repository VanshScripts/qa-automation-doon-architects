from selenium import webdriver
from pages.careers_page import CareersPage
import time

def test_careers_application():
    driver = webdriver.Chrome()

    careers = CareersPage(driver)
    careers.open_careers()

    time.sleep(2)

    careers.open_job_role()
    time.sleep(2)

    careers.click_apply_button()
    time.sleep(2)

    careers.fill_basic_details(
        "Vansh",
        "test@gmail.com",
        "9876543210"
    )

    careers.select_experience()

    import os

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(BASE_DIR, "data", "resume.pdf")

    careers.upload_resume(file_path)

    time.sleep(2)

    careers.submit_form()

    driver.quit()