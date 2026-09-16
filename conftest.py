import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from pages.company_page import CompanyPage
from pages.branch_page import BranchPage


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

    login_page.open()

    login_page.login(
        "superadmin1",
        "admin1234"
    )

    login_page.verify_login_success()

    print("\n========================================")
    print("LOGIN COMPLETED")
    print("========================================")

    return driver
    

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

@pytest.fixture
def company_selected(logged_in_driver):

    driver = logged_in_driver

    company_page = CompanyPage(driver)

    company_page.select_company("Forty Four")

    return driver

@pytest.fixture
def branch_selected(company_selected):

    driver = company_selected

    branch_page = BranchPage(driver)

    branch_page.select_branch("Piliyandala-44")

    return driver