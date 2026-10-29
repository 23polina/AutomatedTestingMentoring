from selenium_module.pages.cart_page import CartPage
from selenium_module.pages.checkout_complete_page import CheckoutCompletePage
from selenium_module.pages.checkout_overview_page import CheckoutOverviewPage
from selenium_module.pages.checkout_page import CheckoutPage
from selenium_module.pages.swag_labs_page import ProductsPage


class Navigator:

    def __init__(self, driver):
        self.driver = driver

    def checkout_page(self):
        return CheckoutPage(self.driver)

    def checkout_complete_page(self):
        return CheckoutCompletePage(self.driver)

    def cart_page(self):
        return CartPage(self.driver)

    def products_page(self):
        return ProductsPage(self.driver)
