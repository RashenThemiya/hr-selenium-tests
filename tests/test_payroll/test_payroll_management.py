from pages.sidebar_page import SidebarPage


def test_payroll_management(branch_selected):

    driver = branch_selected

    sidebar = SidebarPage(driver)

    sidebar.click_payroll_management()

    print("\nPAYROLL MANAGEMENT OPENED")