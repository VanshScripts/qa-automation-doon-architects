from selenium import webdriver

def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://doonarchitects.com")

    assert "doonarchitects" in driver.current_url

    driver.quit()