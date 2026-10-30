from selenium.webdriver.common.by import By
from selenium_module.pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    CONFIRMATION_MESSAGE = (By.XPATH, "//*[@data-test='complete-header']")

    BACK_HOME_BUTTON = (By.ID, "back-to-products")

    def get_confirmation_message(self):
        return self.get_text(self.CONFIRMATION_MESSAGE)

    def get_back_to_product_page(self):
        self.click(self.BACK_HOME_BUTTON)
