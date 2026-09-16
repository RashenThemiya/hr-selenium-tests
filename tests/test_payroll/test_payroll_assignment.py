from pages.sidebar_page import SidebarPage


def test_payroll_assignment(branch_selected):

    driver = branch_selected

    sidebar = SidebarPage(driver)

    # Open Payroll Management
    sidebar.click_payroll_management()

    # Click Payroll Assignment
    sidebar.click_payroll_assignment()

    print("\nPAYROLL ASSIGNMENT OPENED")