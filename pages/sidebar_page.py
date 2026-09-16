from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException
)


class SidebarPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    # ==================================================
    # COMMON OVERLAY
    # ==================================================

    overlay = (
        By.CSS_SELECTOR,
        "div.fixed.inset-0.z-50"
    )

    # ==================================================
    # PAYROLL MANAGEMENT
    # ==================================================

    payroll_management = (
        By.XPATH,
        "//aside[@aria-label='System Owner desktop navigation']"
        "//button[.//span[normalize-space()='Payroll Management']]"
    )

    payroll_assignment = (
        By.XPATH,
        "//aside[@aria-label='System Owner desktop navigation']"
        "//span[normalize-space()='Payroll Assignment']"
    )

    payroll_run = (
        By.XPATH,
        "//aside[@aria-label='System Owner desktop navigation']"
        "//span[normalize-space()='Payroll Run']"
    )

    reimbursements = (
        By.XPATH,
        "//aside[@aria-label='System Owner desktop navigation']"
        "//span[normalize-space()='Reimbursements']"
    )

    # ==================================================
    # WAIT FOR OVERLAY
    # ==================================================

    def wait_for_overlay(self):

        print("Waiting for screen overlay...")

        try:

            self.wait.until(
                lambda driver: not any(
                    element.is_displayed()
                    for element in driver.find_elements(
                        *self.overlay
                    )
                )
            )

            print("Screen overlay is gone.")

        except:

            print("No visible overlay found.")

    # ==================================================
    # PAYROLL MANAGEMENT
    # ==================================================

    def click_payroll_management(self):

        print("\n========================================")
        print("PAYROLL MANAGEMENT")
        print("========================================")

        # Wait for loading/modal overlay
        self.wait_for_overlay()

        print("Waiting for Payroll Management...")

        for attempt in range(3):

            try:

                payroll = self.wait.until(
                    EC.element_to_be_clickable(
                        self.payroll_management
                    )
                )

                print("Payroll Management is clickable.")

                payroll.click()

                print("Payroll Management clicked.")

                return

            except StaleElementReferenceException:

                print(
                    f"Payroll element became stale. "
                    f"Retry {attempt + 1}/3..."
                )

                self.wait_for_overlay()

            except ElementClickInterceptedException:

                print(
                    f"Payroll click intercepted. "
                    f"Retry {attempt + 1}/3..."
                )

                self.wait_for_overlay()

        raise Exception(
            "Could not click Payroll Management after 3 attempts."
        )

    # ==================================================
    # PAYROLL ASSIGNMENT
    # ==================================================

    def click_payroll_assignment(self):

        print("\n========================================")
        print("PAYROLL ASSIGNMENT")
        print("========================================")

        self.wait_for_overlay()

        assignment = self.wait.until(
            EC.element_to_be_clickable(
                self.payroll_assignment
            )
        )

        print("Payroll Assignment is clickable.")

        assignment.click()

        print("Payroll Assignment clicked.")

    # ==================================================
    # PAYROLL RUN
    # ==================================================

    def click_payroll_run(self):

        print("\n========================================")
        print("PAYROLL RUN")
        print("========================================")

        self.wait_for_overlay()

        payroll_run = self.wait.until(
            EC.element_to_be_clickable(
                self.payroll_run
            )
        )

        print("Payroll Run is clickable.")

        payroll_run.click()

        print("Payroll Run clicked.")

    # ==================================================
    # REIMBURSEMENTS
    # ==================================================

    def click_reimbursements(self):

        print("\n========================================")
        print("REIMBURSEMENTS")
        print("========================================")

        self.wait_for_overlay()

        reimbursements = self.wait.until(
            EC.element_to_be_clickable(
                self.reimbursements
            )
        )

        print("Reimbursements is clickable.")

        reimbursements.click()

        print("Reimbursements clicked.")