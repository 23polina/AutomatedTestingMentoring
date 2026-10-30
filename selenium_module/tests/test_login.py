from selenium_module.data.test_data import VALID_USERNAME, PASSWORD, LOCKED_USERNAME, INVALID_USERNAME, INVALID_PASSWORD


def test_successful_login(login_page, navigator):
    """Check login with valid Username and Password"""
    login_page.login(VALID_USERNAME, PASSWORD)
    products_page = navigator.products_page()

    assert products_page.get_page_title() == "Swag Labs"
    assert products_page.get_section_title() == "Products"


def test_locked_out_user(login_page):
    """Check login for Locked Out user"""
    login_page.login_with_invalid_data(LOCKED_USERNAME, PASSWORD)

    assert login_page.get_error_message() == "Epic sadface: Sorry, this user has been locked out."


def test_invalid_username(login_page):
    """Check login for Invalid Username but valid Password"""
    login_page.login_with_invalid_data(INVALID_USERNAME, PASSWORD)

    assert login_page.get_error_message() == "Epic sadface: Username and password do not match any user in this service"


def test_invalid_password(login_page):
    """Check login for valid Username but Invalid Password"""
    login_page.login_with_invalid_data(VALID_USERNAME, INVALID_PASSWORD)

    assert login_page.get_error_message() == "Epic sadface: Username and password do not match any user in this service"
