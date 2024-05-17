import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options as ChromeOptions

# The webdriver management will be handled by the browserstack-sdk
# so this will be overridden and tests will run browserstack -
# without any changes to the test files!
options = ChromeOptions()
options.set_capability('sessionName', 'BStack Sample Test')
driver = webdriver.Chrome(options=options)

try:
    try:
    # Open BrowserStack login page
    driver.get("https://www.browserstack.com/users/sign_in")

    # Log in
    username_input = driver.find_element(By.ID, "user_email_login")
    password_input = driver.find_element(By.ID, "user_password")
    login_button = driver.find_element(By.ID, "user_submit")

    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    login_button.click()

    # Wait for homepage to load and assert 'Invite Users' link
    wait = WebDriverWait(driver, 10)
    invite_users_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Invite Users")))

    # Retrieve and print the URL of 'Invite Users' link
    invite_users_url = invite_users_link.get_attribute('href')
    print(f"Invite Users URL: {invite_users_url}")

    # Log out
    profile_menu = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".profile-menu")))
    profile_menu.click()
    logout_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
    logout_button.click()

    print("Logged out successfully.")
finally:
    # Stop the driver
    driver.quit()
