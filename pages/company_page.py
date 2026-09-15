from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CompanyPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def select_company(self, company_name):

        print("\n========================================")
        print("SELECTING COMPANY")
        print("========================================")

        print(f"Waiting for company: {company_name}")

        company_locator = (
            By.XPATH,
            f"//*[normalize-space()='{company_name}']"
        )

        company = self.wait.until(
            EC.element_to_be_clickable(company_locator)
        )

        print(f"Company found: {company_name}")

        company.click()

        print(f"Company selected: {company_name}")