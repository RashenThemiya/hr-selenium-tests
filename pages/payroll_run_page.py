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

    #Inputs Save Changes
    save_changes = (
        By.XPATH,
        "//button[normalize-space()='Save changes']"
    )

    # Finalise all
    finalise_all = (
        By.XPATH,
        "//button[normalize-space()='Finalise all']"
    )

    # Next: Earnings 
    next_earnings = (
        By.XPATH,
        "//button[normalize-space()='Next: Earnings']"
    )

    # Deductions
    deductions = (
        By.XPATH,
        "//button[normalize-space()='Next: Deductions']"
    )

    # Reimbursements
    reimbursements = (
        By.XPATH,
        "//button[normalize-space()='Next: Reimbursements']"
    )

    #No Pay
    no_pay = (
        By.XPATH,
        "//button[normalize-space()='Next: No-pay']"
    )

    # Time adj
    time_adj = (
        By.XPATH,
        "//button[normalize-space()='Next: Time adj.']"
    )

    # Statutory
    statutory = (
        By.XPATH,
        "//button[normalize-space()='Next: Statutory']"
    )

    #Generate statutory
    generate_statutory = (
        By.XPATH,
         "//button[normalize-space()='Generate']"
    )

    #Month Tax
    month_tax = (
        By.XPATH,
        "//button[contains(normalize-space(.), 'Next: Month tax')]"
    )

    #Generate Month Tax
    generate_month_tax = (
        By.XPATH,
         "//button[contains(normalize-space(.), 'Generate')]"
    )

    #Save Generated Month Taxes
    save_taxable = (
        By.XPATH,
        "//button[contains(normalize-space(.), 'Save taxable')]"
    )

    # Special Earnings
    special_earnings = (
        By.XPATH,
        "//button[contains(normalize-space(.), 'Next: Special earnings')]"
    )

    # SE Tax
    se_tax = (
        By.XPATH,
        "//button[contains(normalize-space(.), 'Next: SE Tax')]"
    )

    # Adjustments
    adjustments = (
        By.XPATH,
        "//button[contains(normalize-space(.), 'Next: Adjustments')]"
    )

    # next: Finalized
    next_finalized = (
        By.XPATH,
        "//button[contains(normalize-space(.), 'Next: Finalize')]"
    )

    #Finalize payroll run
    finalize_payroll_run = (
        By.XPATH,
        "//button[contains(normalize-space(.), 'Finalize payroll run')]"
    )

    # Yes, finalize
    yes_finalize = (
        By.XPATH,
        "//button[contains(normalize-space(.), 'Yes, finalize')]"
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

    def click_save_changes(self):

        print("\n========================================")
        print("SAVE CHANGES")
        print("========================================")

        self.wait_for_overlay()

        print("Waiting for Save changes button...")

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.save_changes
            )
        )

        print("Save changes button is clickable.")

        button.click()

        print("Save changes button clicked.")

    def click_finalise_all(self):

        print("\n========================================")
        print("FINALISE ALL")
        print("========================================")

        self.wait_for_overlay()

        print("Waiting for Finalise all button...")

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.finalise_all
            )
        )

        print("Finalise all button is clickable.")

        button.click()

        print("Finalise all button clicked.")

    def click_next_earnings(self):

        print("\n========================================")
        print("NEXT: EARNINGS")
        print("========================================")

        self.wait_for_overlay()

        print("Waiting for Next: Earnings button...")

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.next_earnings
            )
        )

        print("Next: Earnings button is clickable.")

        button.click()

        print("Next: Earnings button clicked.")

    def click_deductions(self):

        print("\n========================================")
        print("NEXT: DEDUCTIONS")
        print("========================================")

        self.wait_for_overlay()

        print("Waiting for Next: Deductions button...")

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.deductions
            )
        )

        print("Next: Deductions button is clickable.")

        button.click()

        print("Next: Deductions button clicked.")

    def click_reimbursements(self):

        print("\n========================================")
        print("NEXT: REIMBURSEMENTS")
        print("========================================")

        self.wait_for_overlay()

        print("Waiting for Next: Reimbursements button...")

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.reimbursements
            )
        )

        print("Next: Reimbursements button is clickable.")

        button.click()

        print("Next: Reimbursements button clicked.")

    def click_no_pay(self):

        print("\n========================================")
        print("NEXT: NO PAY")
        print("========================================")

        self.wait_for_overlay()

        print("Waiting for Next: No Pay button...")

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.no_pay
            )
        )

        print("Next: No Pay button is clickable.")

        button.click()

        print("Next: No Pay button clicked.")

    def click_time_adj(self):

        print("\n========================================")
        print("NEXT: TIME ADJ.")
        print("========================================")

        self.wait_for_overlay()

        print("Waiting for Next: Time adj. button...")

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.time_adj
            )
        )

        print("Next: Time adj. button is clickable.")

        button.click()

        print("Next: Time adj. button clicked.")

    def click_statutory(self):

        print("\n========================================")
        print("NEXT: STATUTORY")
        print("========================================")

        self.wait_for_overlay()

        print("Waiting for Next: Statutory button...")

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.statutory
            )
        )

        print("Next: Statutory button is clickable.")

        button.click()

        print("Next: Statutory button clicked.")

    def click_generate_statutory(self):

        print("\n========================================")
        print("GENERATE STATUTORY")
        print("========================================")

        self.wait_for_overlay()

        print("Waiting for Generate button...")

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.generate_statutory
            )
        )

        print("Generate button is clickable.")

        button.click()

        print("Generate button clicked.")

    def click_month_tax(self):

        print("\n========================================")
        print("NEXT: MONTH TAX")
        print("========================================")

        self.wait_for_overlay()

        print("Waiting for Next: Month Tax button...")

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.month_tax
            )
        )

        print("Next: Month Tax button is clickable.")

        button.click()

        print("Next: Month Tax button clicked.")

    def click_generate_month_tax(self):

        print("\n========================================")
        print("GENERATE MONTH TAX")
        print("========================================")

        self.wait_for_overlay()

        print("Waiting for Generate button...")

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.generate_month_tax
            )
        )

        print("Generate button is clickable.")

        button.click()

        print("Generate button clicked.")

    def click_save_taxable(self):

        print("\n========================================")
        print("SAVE TAXABLE")
        print("========================================")

        self.wait_for_overlay()

        print("Waiting for Save changes button...")

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.save_taxable
            )
        )

        print("Save changes button is clickable.")

        button.click()

        print("Save changes button clicked.")

    def click_special_earnings(self):

        print("\n========================================")
        print("NEXT: SPECIAL EARNINGS")
        print("========================================")

        self.wait_for_overlay()

        print("Waiting for Next: Special Earnings button...")

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.special_earnings
            )
        )

        print("Next: Special Earnings button is clickable.")

        button.click()

        print("Next: Special Earnings button clicked.")

    def click_se_tax(self):

        print("\n========================================")
        print("NEXT: SE TAX")
        print("========================================")

        self.wait_for_overlay()

        print("Waiting for Next: SE Tax button...")

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.se_tax
            )
        )

        print("Next: SE Tax button is clickable.")

        button.click()

        print("Next: SE Tax button clicked.")

    def click_adjustments(self):
        print("\n========================================")
        print("NEXT: ADJUSTMENTS")
        print("========================================")

        self.wait_for_overlay()

        print("Waiting for Next: Adjustments button...")

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.adjustments
            )
        )

        print("Next: Adjustments button is clickable.")

        button.click()

        print("Next: Adjustments button clicked.")

    def click_next_finalized(self):

        print("\n========================================")
        print("NEXT: FINALIZED")
        print("========================================")

        self.wait_for_overlay()

        print("Waiting for Next: Finalize button...")

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.next_finalized
            )
        )

        print("Next: Finalize button is clickable.")

        button.click()

        print("Next: Finalize button clicked.")

    def click_finalize_payroll_run(self):

        print("\n========================================")
        print("FINALIZE PAYROLL RUN")
        print("========================================")

        self.wait_for_overlay()

        print("Waiting for Finalize payroll run button...")

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.finalize_payroll_run
            )
        )

        print("Finalize payroll run button is clickable.")

        button.click()

        print("Finalize payroll run button clicked.")

    def click_yes_finalize(self):

        print("\n========================================")
        print("YES, FINALIZE")
        print("========================================")

        self.wait_for_overlay()

        print("Waiting for Yes, finalize button...")

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.yes_finalize
            )
        )

        print("Yes, finalize button is clickable.")

        button.click()

        print("Yes, finalize button clicked.")


