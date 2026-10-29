from selenium.webdriver.common.by import By
from selenium_module.pages.base_page import BasePage
from selenium_module.pages.checkout_overview_page import CheckoutOverviewPage


class CheckoutPage(BasePage):

    FIST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    ZIP_POSTAL_CODE_FIELD = (By.ID, "postal-code")
    CANCEL_BUTTON = (By.ID, "cancel")
    CONTINUE_BUTTON = (By.ID, "continue")

    def fill_in_submit_checkout_form(self, firstname, lastname, postalcode):
        self.enter_value(self.FIST_NAME_FIELD, firstname)
        self.enter_value(self.LAST_NAME_FIELD, lastname)
        self.enter_value(self.ZIP_POSTAL_CODE_FIELD, postalcode)
        self.click(self.CONTINUE_BUTTON)
        return CheckoutOverviewPage(self.driver)
