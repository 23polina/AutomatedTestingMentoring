from selenium.webdriver.common.by import By
from selenium_module.pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):

    CHECKOUT_ITEMS = (By.XPATH, "//div[@class='inventory_item_name']")
    FINISH_BUTTON = (By.ID, "finish")
    PRICE = (By.XPATH,
             "//div[@data-test='inventory-item-name'][normalize-space()='{product_name}']/ancestor::div[@data-test='inventory-item']//div[@class='inventory_item_price']")

    ITEM_TOTAL_PRICE = (By.CLASS_NAME, "summary_subtotal_label")
    TAX_AMOUNT= (By.CLASS_NAME, "summary_tax_label")
    TOTAL_PRICE = (By.CLASS_NAME, "summary_total_label")

    def get_items_in_checkout(self):
        return [item.text for item in self.find_all(self.CHECKOUT_ITEMS)]

    def get_price(self, product_name):
        by, value = self.PRICE
        return self.get_text((by, value.format(product_name=product_name)))

    def get_tax(self):
        return self.get_text(self.TAX_AMOUNT)

    def get_item_total_price(self):
        return self.get_text(self.ITEM_TOTAL_PRICE)

    def get_total_price_with_tax(self):
        return self.get_text(self.TOTAL_PRICE)

    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)
