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

    payroll_run.enter_period_start("08/25/2026")

    payroll_run.enter_period_end("09/25/2026")

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
    payroll_run.click_save_changes()
    payroll_run.click_finalise_all()
    payroll_run.click_next_earnings()
    payroll_run.click_deductions()
    payroll_run.click_reimbursements()
    payroll_run.click_no_pay()
    payroll_run.click_time_adj()
    payroll_run.click_statutory()
    payroll_run.click_generate_statutory()
    payroll_run.click_month_tax()
    payroll_run.click_generate_month_tax()
    payroll_run.click_save_taxable()
    payroll_run.click_special_earnings()
    payroll_run.click_se_tax()
    payroll_run.click_adjustments()
    payroll_run.click_next_finalized()
    payroll_run.click_finalize_payroll_run()
    payroll_run.click_yes_finalize()
    print("\n========================================")
    print("PAYROLL RUN CREATED SUCCESSFULLY")
    print("========================================")

    input(
            "\nPress ENTER to close browser..."
        )