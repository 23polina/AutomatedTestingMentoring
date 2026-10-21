from selenium.webdriver.common.by import By
from selenium_module.pages.base_page import BasePage
from selenium_module.pages.swag_labs_page import SwagLabs


class LoginPage(BasePage):

    URL = "https://www.saucedemo.com/"
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, "//div[@class='error-message-container error']")

    def open_page(self):
        self.open(self.URL)

    def fill_and_submit(self, username, password):
        self.enter_value(self.USERNAME_FIELD, username)
        self.enter_value(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        self.fill_and_submit(username, password)
        return SwagLabs(self.driver)

    def login_with_invalid_data(self, username, password):
        self.fill_and_submit(username, password)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
