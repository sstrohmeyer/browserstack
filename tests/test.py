from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Read credentials from environment variables
USERNAME = os.getenv('SERVICE_CREDS_USR')
PASSWORD = os.getenv('SERVICE_CREDS_PSW')

# Debug: Print the credentials to ensure they are correctly set
print(f"USERNAME: {USERNAME}")
print(f"PASSWORD: {PASSWORD}")

# Check if credentials are retrieved correctly
if not USERNAME or not PASSWORD:
    raise ValueError("Username or Password environment variables are not set")


# Initialize WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless Chrome
service = Service(os.getenv('CHROME_DRIVER_PATH'))  # Path to your ChromeDriver

driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Open BrowserStack login page
    driver.get("https://www.browserstack.com/users/sign_in")

    # Wait for the login page to load
    wait = WebDriverWait(driver, 10)
    username_input = wait.until(EC.presence_of_element_located((By.ID, "user_email_login")))

    # Log in
    password_input = driver.find_element(By.ID, "user_password")
    login_button = driver.find_element(By.ID, "user_submit")

    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    login_button.click()

    # Wait for homepage to load and assert 'Invite Users' link
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
    # Close the browser
    driver.quit()
