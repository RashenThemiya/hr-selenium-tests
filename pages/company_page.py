from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CompanyPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

        self.forty_four_company = (
            By.XPATH,
            "//*[normalize-space()='Forty Four']"
        )

    def select_forty_four(self):

        print("\n========================================")
        print("SELECTING COMPANY")
        print("========================================")

        print("Waiting for Forty Four company...")

        company = self.wait.until(
            EC.element_to_be_clickable(
                self.forty_four_company
            )
        )

        print("Forty Four company found.")

        company.click()

        print("Forty Four company clicked.")