from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LogoutPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

        self.logout_button = (
            By.XPATH,
            "//button[contains(., 'Logout')]"
        )

    def logout(self):

        print("\n========================================")
        print("LOGOUT")
        print("========================================")

        print("Waiting for logout button...")

        logout_button = self.wait.until(
            EC.element_to_be_clickable(
                self.logout_button
            )
        )

        print("Logout button found.")

        logout_button.click()

        print("Logout button clicked.")

    def verify_logout(self):

        print("\nWaiting for logout response...")

        self.wait.until(
            lambda driver:
            "#/admin/login" in driver.current_url
        )

        print("Logout successful.")

        print("Current URL:")
        print(self.driver.current_url)

        return True