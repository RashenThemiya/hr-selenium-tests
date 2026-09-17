from pages.sidebar_page import SidebarPage
from pages.payroll_run_page import PayrollRunPage


def test_create_payroll_run(branch_selected):

    driver = branch_selected

    sidebar = SidebarPage(driver)
    payroll_run = PayrollRunPage(driver)

    # =========================================
    # OPEN PAYROLL MANAGEMENT
    # =========================================

    sidebar.click_payroll_management()

    # =========================================
    # OPEN PAYROLL RUN
    # =========================================

    sidebar.click_payroll_run()

    # =========================================
    # CREATE NEW PAYROLL RUN
    # =========================================

    payroll_run.click_new_run()

    # =========================================
    # ENTER PAYROLL DETAILS
    # =========================================

    payroll_run.enter_period_start("01/25/2026")

    payroll_run.enter_period_end("02/25/2026")

    # payroll_run.enter_payroll_month("April 2026")

    payroll_run.select_currency("LKR — Sri Lanka Rupees")

    # =========================================
    # CREATE PAYROLL RUN
    # =========================================

    payroll_run.click_create_run()
    payroll_run.click_select_all()
    payroll_run.click_generate_draft()
    payroll_run.click_generate_attendance()
    payroll_run.click_present_days()
    payroll_run.enter_present_days_input("30")
    payroll_run.click_enter_inputs()
    print("\n========================================")
    print("PAYROLL RUN DETAILS ENTERED")
    print("========================================")

    input(
            "\nPress ENTER to close browser..."
        )