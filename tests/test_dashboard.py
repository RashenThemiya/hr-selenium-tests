def test_dashboard(logged_in_driver):

    driver = logged_in_driver

    print("\n========================================")
    print("DASHBOARD TEST")
    print("========================================")

    print("Current URL:", driver.current_url)

    assert "#/super-admin/dashboard" in driver.current_url

    print("Dashboard test passed.")

    