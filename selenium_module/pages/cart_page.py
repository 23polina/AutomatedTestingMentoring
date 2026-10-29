from selenium.webdriver.common.by import By
from selenium_module.pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = (By.XPATH, "//*[@data-test='inventory-item-name']")
    REMOVE_BUTTON = (By.XPATH, "//div[@data-test='inventory-item-name'][normalize-space()='{product_name}']/ancestor::div[@data-test='inventory-item']//button[contains(@id, 'remove')]")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    PRICE = (By.XPATH, "//div[@data-test='inventory-item-name'][normalize-space()='{product_name}']/ancestor::div[@data-test='inventory-item']//div[@class='inventory_item_price']")


    def get_items_in_cart(self):
        return [item.text for item in self.find_all(self.CART_ITEMS)]

    def get_price(self, product_name):
        by, value = self.PRICE
        return self.get_text((by, value.format(product_name=product_name)))

    def remove_item_from_cart_page(self, product_name):
        by, value = self.REMOVE_BUTTON
        self.click((by, value.format(product_name=product_name)))

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BUTTON)

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)
