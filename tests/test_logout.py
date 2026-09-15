from pages.logout_page import LogoutPage


def test_logout(logged_in_driver):

    driver = logged_in_driver

    print("\n========================================")
    print("LOGOUT TEST")
    print("========================================")

    logout_page = LogoutPage(driver)

    logout_page.logout()

    assert logout_page.verify_logout()

    print("\nLOGOUT TEST PASSED")