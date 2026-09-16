from pages.sidebar_page import SidebarPage


def test_reimbursements(branch_selected):

    driver = branch_selected

    sidebar = SidebarPage(driver)

    # Open Payroll Management
    sidebar.click_payroll_management()

    # Click Reimbursements
    sidebar.click_reimbursements()

    print("\nREIMBURSEMENTS OPENED")