from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException
)


class PayrollRunPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    # ==================================================
    # OVERLAY
    # ==================================================

    overlay = (
        By.CSS_SELECTOR,
        "div.fixed.inset-0.z-50"
    )

    # ==================================================
    # NEW RUN BUTTON
    # ==================================================

    new_run_button = (
        By.XPATH,
        "//button[normalize-space()='New run']"
    )

    # ==================================================
    # NEW PAYROLL RUN FORM
    # ==================================================

    # Period Start
    period_start = (
        By.XPATH,
        "(//input[@type='date'])[1]"
    )

    # Period End
    period_end = (
        By.XPATH,
        "(//input[@type='date'])[2]"
    )

    # Payroll Month
    payroll_month = (
        By.XPATH,
        "(//input[@type='month'])[1]"
    )

    # Currency
    currency = (
        By.XPATH,
        "//select"
    )
    # Create Run Button
    create_run_button = (
        By.XPATH,
        "//button[normalize-space()='Create run']"
    )

    #Select all
    select_all = (
        By.XPATH,
        "//button[normalize-space()='Select all']"
    )

    #Generate Draft
    generate_draft = (
        By.XPATH,
        "//button[normalize-space()='Generate drafts']"
    )

    #Generate Attendance
    generate_attendance = (
        By.XPATH,
        "//button[normalize-space()='Generate']"
    )

    #Present Days
    present_days = (
        By.XPATH,
        "//th[.//div[normalize-space()='Present days']]"
    )

    #Input Days
    present_days_input = (
    By.XPATH,
    "//input[@type='number' and @placeholder='value']"
    )

    #Enter Present Days Input
    enter_inputs = (
    By.XPATH,
    "//button[contains(normalize-space(.), '↵') and not(@disabled)]"
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
    # CLICK NEW RUN
    # ==================================================

    def click_new_run(self):

        print("\n========================================")
        print("NEW PAYROLL RUN")
        print("========================================")

        self.wait_for_overlay()

        print("Waiting for New run button...")

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.new_run_button
            )
        )

        print("New run button is clickable.")

        button.click()

        print("New run button clicked.")

    # ==================================================
    # ENTER PERIOD START
    # ==================================================

    def enter_period_start(self, date):

        print("\nEntering Period Start...")

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.period_start
            )
        )

        print("Period Start field found.")

        field.send_keys(date)

        print(f"Period Start entered: {date}")

    # ==================================================
    # ENTER PERIOD END
    # ==================================================

    def enter_period_end(self, date):

        print("\nEntering Period End...")

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.period_end
            )
        )

        print("Period End field found.")

        field.send_keys(date)

        print(f"Period End entered: {date}")

    # ==================================================
    # ENTER PAYROLL MONTH
    # ==================================================

    def enter_payroll_month(self, month):

        print("\nEntering Payroll Month...")

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.payroll_month
            )
        )

        print("Payroll Month field found.")

        field.send_keys(month)

        print(f"Payroll Month entered: {month}")

    # ==================================================
    # SELECT CURRENCY
    # ==================================================

    def select_currency(self, currency):

        print("\nSelecting Currency...")

        select = self.wait.until(
            EC.element_to_be_clickable(
                self.currency
            )
        )

        select.click()

        option = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//option[normalize-space()='{currency}']"
                )
            )
        )

        option.click()

        print(f"Currency selected: {currency}")

        #create run button

    def click_create_run(self):

        print("\n========================================")
        print("CREATE PAYROLL RUN")
        print("========================================")

        self.wait_for_overlay()

        print("Waiting for Create run button...")

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.create_run_button
            )
        )

        print("Create run button is clickable.")

        button.click()

        print("Create run button clicked.")

        #select all button
    def click_select_all(self):

        print("\n========================================")
        print("SELECT ALL EMPLOYEES")
        print("========================================")

        self.wait_for_overlay()

        print("Waiting for Select all button...")

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.select_all
            )
        )

        print("Select all button is clickable.")

        button.click()

        print("Select all button clicked.")

        #generate draft button
    def click_generate_draft(self):

        print("\n========================================")
        print("GENERATE DRAFTS")
        print("========================================")

        self.wait_for_overlay()

        print("Waiting for Generate drafts button...")

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.generate_draft
            )
        )

        print("Generate drafts button is clickable.")

        button.click()

        print("Generate drafts button clicked.")

        #generate attendance button
    def click_generate_attendance(self):

        print("\n========================================")
        print("GENERATE ATTENDANCE")
        print("========================================")

        self.wait_for_overlay()

        print("Waiting for Generate button...")

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.generate_attendance
            )
        )

        print("Generate button is clickable.")

        button.click()

        print("Generate button clicked.")

        #present days button
    def click_present_days(self):

        print("\n========================================")
        print("PRESENT DAYS")
        print("========================================")

        self.wait_for_overlay()

        print("Waiting for Present days button...")

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.present_days
            )
        )

        print("Present days button is clickable.")

        button.click()

        print("Present days button clicked.")

        #present days input
    def enter_present_days_input(self, days):

        print("\nEntering Present Days...")

        field = self.wait.until(
            EC.visibility_of_element_located(
                self.present_days_input
            )
        )

        field.click()
        field.clear()
        field.send_keys(str(days))
        print(f"Present Days entered: {days}")

        # Move focus away from the input
        field.send_keys("\t")

        print("Present Days input focus changed.")

        #enter inputs button
    def click_enter_inputs(self):
        print("\n========================================")
        print("ENTER INPUTS")
        print("========================================")

        self.wait_for_overlay()

        print("Waiting for Enter button...")

        button = self.wait.until(
            EC.presence_of_element_located(self.enter_inputs)
        )

        print("Enter button found.")
        print("Button text:", repr(button.text))
        print("Button enabled:", button.is_enabled())
        print("Button displayed:", button.is_displayed())

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            button,
        )

        self.wait.until(
            lambda driver: button.is_displayed() and button.is_enabled()
        )

        button.click()

        print("Enter button clicked.")
