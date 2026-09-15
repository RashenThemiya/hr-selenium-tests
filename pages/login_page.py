from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

        # =========================================
        # Login Page Elements
        # =========================================

        self.username_field = (
            By.NAME,
            "username"
        )

        self.password_field = (
            By.NAME,
            "password"
        )

        self.login_button = (
            By.XPATH,
            "//button[contains(., 'Sign In')]"
        )

    # =============================================
    # Open Login Page
    # =============================================

    def open(self):

        self.driver.get(
            "https://hr-system-frontend-beta.vercel.app/#/admin/login"
        )

        print("========================================")
        print("LOGIN PAGE")
        print("========================================")

        print("Current URL:", self.driver.current_url)

    # =============================================
    # Enter Username
    # =============================================

    def enter_username(self, username):

        print("\nWaiting for username...")

        username_field = self.wait.until(
            EC.visibility_of_element_located(
                self.username_field
            )
        )

        username_field.clear()
        username_field.send_keys(username)

        print("Username entered.")

    # =============================================
    # Enter Password
    # =============================================

    def enter_password(self, password):

        print("\nWaiting for password...")

        password_field = self.wait.until(
            EC.visibility_of_element_located(
                self.password_field
            )
        )

        password_field.clear()
        password_field.send_keys(password)

        print("Password entered.")

    # =============================================
    # Complete CAPTCHA
    # =============================================

    def complete_recaptcha(self):

        print("\n========================================")
        print("RECAPTCHA")
        print("========================================")

        input(
            "Complete the reCAPTCHA manually, "
            "then press ENTER..."
        )

    # =============================================
    # Click Login
    # =============================================

    def click_login(self):

        print("\nWaiting for Sign In button...")

        login_button = self.wait.until(
            EC.element_to_be_clickable(
                self.login_button
            )
        )

        print("Login button found.")

        login_button.click()

        print("Login button clicked.")

    # =============================================
    # Complete Login
    # =============================================

    def login(self, username, password):

        self.enter_username(username)

        self.enter_password(password)

        self.complete_recaptcha()

        self.click_login()

    # =============================================
    # Verify Dashboard
    # =============================================

    def verify_login_success(self):

        print("\nWaiting for application response...")

        self.wait.until(
            lambda driver:
            "#/super-admin/dashboard" in driver.current_url
        )

        print("\n========================================")
        print("LOGIN SUCCESS")
        print("========================================")

        print("Current URL:")
        print(self.driver.current_url)

        return True