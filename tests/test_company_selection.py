from pages.company_page import CompanyPage


def test_select_forty_four(logged_in_driver):

    driver = logged_in_driver

    company_page = CompanyPage(driver)

    company_page.select_forty_four()

    print("\nFORTY FOUR COMPANY SELECTION TEST PASSED") 