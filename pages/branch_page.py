from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BranchPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def select_branch(self, branch_name):

        print("\n========================================")
        print("SELECTING BRANCH")
        print("========================================")

        print(f"Waiting for branch: {branch_name}")

        branch_locator = (
            By.XPATH,
            f"//*[normalize-space()='{branch_name}']"
        )

        branch = self.wait.until(
            EC.element_to_be_clickable(branch_locator)
        )

        print(f"Branch found: {branch_name}")

        branch.click()

        print(f"Branch selected: {branch_name}")