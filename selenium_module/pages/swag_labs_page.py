from selenium.webdriver.common.by import By
from selenium_module.pages.base_page import BasePage


class ProductsPage(BasePage):
    PAGE_TITLE = (By.CLASS_NAME, "app_logo")
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    PRODUCT_BUTTON = (
        By.XPATH,
        "//div[@data-test='inventory-item-name'][normalize-space()='{product_name}']/ancestor::div[@data-test='inventory-item']//button"
    )
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def get_section_title(self):
        return self.get_text(self.PRODUCTS_TITLE)

    def toggle_item_button(self, product_name):
        by, value = self.PRODUCT_BUTTON
        return by, value.format(product_name=product_name)

    def add_item_to_cart(self, product_name):
        self.click(self.toggle_item_button(product_name))

    def remove_item_from_cart(self, product_name):
        self.click(self.toggle_item_button(product_name))

    def get_button_text(self, product_name):
        return self.get_text(self.toggle_item_button(product_name=product_name))

    def get_cart_amount(self):
        return int(self.get_text(self.CART_BADGE))

    def go_to_cart(self):
        self.click(self.CART_BADGE)
