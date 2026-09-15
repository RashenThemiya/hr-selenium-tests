from pages.login_page import LoginPage


def test_login(driver):

    # =========================================
    # Create Login Page
    # =========================================

    login_page = LoginPage(driver)

    # =========================================
    # Open Login Page
    # =========================================

    login_page.open()

    # =========================================
    # Login
    # =========================================

    login_page.login(
        "superadmin1",
        "admin1234"
    )

    # =========================================
    # Verify Login
    # =========================================

    assert login_page.verify_login_success()

    print("\nLOGIN TEST PASSED")

    # =========================================
    # Keep Browser Open
    # =========================================

    input(
        "\nPress ENTER to close browser..."
    )