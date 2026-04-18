from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login():
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Test Data
    url = "https://the-internet.herokuapp.com/login"
    username = "tomsmith"
    password = "SuperSecretPassword!"

    # Step 1: Open Website
    driver.get(url)

    # Step 2: Enter Username
    driver.find_element(By.ID, "username").send_keys(username)

    # Step 3: Enter Password
    driver.find_element(By.ID, "password").send_keys(password)

    # Step 4: Click Login
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Step 5: Validate Result
    success_msg = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in success_msg
    print("Second version of login test")
    print("Third version of login test")
    driver.quit()