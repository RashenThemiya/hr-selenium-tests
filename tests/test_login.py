from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_login():

    driver = webdriver.Chrome()
    driver.maximize_window()

    try:

        # =========================================
        # Open Login Page
        # =========================================

        login_url = (
            "https://hr-system-frontend-beta.vercel.app/#/admin/login"
        )

        dashboard_url = (
            "https://hr-system-frontend-beta.vercel.app/#/super-admin/dashboard"
        )

        driver.get(login_url)

        wait = WebDriverWait(driver, 30)

        print("========================================")
        print("LOGIN PAGE")
        print("========================================")
        print("Current URL:", driver.current_url)


        # =========================================
        # Username
        # =========================================

        print("\nWaiting for username...")

        username = wait.until(
            EC.visibility_of_element_located(
                (By.NAME, "username")
            )
        )

        username.clear()
        username.send_keys("superadmin1")

        print("Username entered.")


        # =========================================
        # Password
        # =========================================

        print("\nWaiting for password...")

        password = wait.until(
            EC.visibility_of_element_located(
                (By.NAME, "password")
            )
        )

        password.clear()
        password.send_keys("admin1234")

        print("Password entered.")


        # =========================================
        # Manual reCAPTCHA
        # =========================================

        print("\n========================================")
        print("RECAPTCHA")
        print("========================================")

        input(
            "Complete the reCAPTCHA manually, "
            "then press ENTER..."
        )


        # =========================================
        # Login Button
        # =========================================

        print("\nWaiting for Sign In button...")

        login_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(., 'Sign In')]"
                )
            )
        )

        print("Login button found.")

        login_button.click()

        print("Login button clicked.")


        # =========================================
        # Wait
        # =========================================

        print("\nWaiting for application response...")

        time.sleep(5)


        # =========================================
        # RESULT URL
        # =========================================

        print("\n========================================")
        print("LOGIN RESULT")
        print("========================================")

        print("Current URL:")
        print(driver.current_url)


        # =========================================
        # Keep Browser Open
        # =========================================

        input(
            "\nPress ENTER to close browser..."
        )


    finally:

        driver.quit()


test_login()