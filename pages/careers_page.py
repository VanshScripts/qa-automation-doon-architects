from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CareersPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_careers(self):
        self.driver.get("https://doonarchitects.com/careers")

        # wait for page to load properly
        self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

    # Step 1: Click job card
    def open_job_role(self):
        job = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[.//h3[contains(text(),'Senior Architect')]]")
            )
        )

        self.driver.execute_script("arguments[0].scrollIntoView(true);", job)
        self.wait.until(EC.element_to_be_clickable(job))
        self.driver.execute_script("arguments[0].click();", job)
    # Step 2: Click Apply button
    def click_apply_button(self):
        apply_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(.,'Apply for This Role')]")
            )
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", apply_btn)
        self.driver.execute_script("arguments[0].click();", apply_btn)

    # Step 3: Fill form
    def fill_basic_details(self, name, email, phone):
        self.wait.until(
            EC.visibility_of_element_located((By.NAME, "name"))
        ).send_keys(name)

        self.driver.find_element(By.NAME, "email").send_keys(email)

        # phone input (no name attribute)
        self.driver.find_element(By.XPATH, "//input[@type='tel']").send_keys(phone)

    # Step 4: Select experience
    def select_experience(self):
        years = self.wait.until(
            EC.element_to_be_clickable((By.NAME, "experienceYears"))
        )
        years.click()
        years.find_element(By.XPATH, ".//option[@value='1']").click()

        months = self.wait.until(
            EC.element_to_be_clickable((By.NAME, "experienceMonths"))
        )
        months.click()
        months.find_element(By.XPATH, ".//option[@value='1']").click()

    # Step 5: Upload resume
    def upload_resume(self, file_path):
        upload_input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
        )
        upload_input.send_keys(file_path)

    # Step 6: Submit form
    def submit_form(self):
        submit_btn = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[contains(.,'Submit Application')]")
            )
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
        self.driver.execute_script("arguments[0].click();", submit_btn)