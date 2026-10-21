import pytest
from selenium import webdriver
from selenium_module.data.test_data import VALID_USERNAME, PASSWORD
from selenium_module.pages.login_page import LoginPage


@pytest.fixture
def driver():
    """Create a Chrome WebDriver for a single test.
    Opens Chrome with a 1920x1080 window and yields the driver to the test"""
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def login_page(driver):
    """""Open the login page without logging in.
    Returns the opened login page"""
    page = LoginPage(driver)
    page.open_page()
    return page


@pytest.fixture()
def login_into_swag_labs(driver):
    """Log in as a valid user and land on the products page.
    Returns the products page after a successful login"""
    login_page = LoginPage(driver)
    login_page.open_page()
    return login_page.login(VALID_USERNAME, PASSWORD)


@pytest.fixture()
def added_products(login_into_swag_labs):
    """Add two products to the cart and open the cart page.
    Returns the cart page with both products inside"""
    login_into_swag_labs.add_item_to_cart("Sauce Labs Backpack")
    login_into_swag_labs.add_item_to_cart("Sauce Labs Bike Light")
    cart_page = login_into_swag_labs.go_to_cart()
    return cart_page
