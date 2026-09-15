import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage


@pytest.fixture
def driver():

    print("\nStarting Chrome...")

    driver = webdriver.Chrome()

    driver.maximize_window()

    yield driver

    print("\nClosing Chrome...")

    driver.quit()

@pytest.fixture
def login_only(driver):

    print("\n========================================")
    print("STARTING LOGIN")
    print("========================================")

    login_page = LoginPage(driver)

    # Open login page
    login_page.open()

    # Login
    login_page.login(
        "superadmin1",
        "admin1234"
    )

    # Verify login
    login_page.verify_login_success()

    print("\n========================================")
    print("LOGIN COMPLETED")
    print("========================================")

    return driver
    
    # =========================================
    # Logout
    # =========================================

@pytest.fixture
def logged_in_driver(login_only):

    driver = login_only

    yield driver

    print("\n========================================")
    print("STARTING AUTOMATIC LOGOUT")
    print("========================================")

    logout_page = LogoutPage(driver)

    try:

        logout_page.logout()

        logout_page.verify_logout()

        print("\nLOGOUT COMPLETED")

    except Exception as e:

        print("\nLogout failed:")
        print(e)