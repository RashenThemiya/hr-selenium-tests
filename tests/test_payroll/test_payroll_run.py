from pages.sidebar_page import SidebarPage


def test_payroll_run(branch_selected):

    driver = branch_selected

    sidebar = SidebarPage(driver)

    # Open Payroll Management
    sidebar.click_payroll_management()

    # Click Payroll Run
    sidebar.click_payroll_run()

    print("\nPAYROLL RUN OPENED")