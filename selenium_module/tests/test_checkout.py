from selenium_module.data.test_data import FIRST_NAME, LAST_NAME, ZIP_POSTAL_CODE


def test_calculation_price_correctness(added_products):
    """Check that item's price is displayed correctly and total price is calculated correctly during checkout process"""
    checkout_page = added_products.checkout()
    overview_page = checkout_page.fill_in_submit_checkout_form(FIRST_NAME, LAST_NAME, ZIP_POSTAL_CODE)

    assert overview_page.get_price("Sauce Labs Backpack") == "$29.99"
    assert overview_page.get_price("Sauce Labs Bike Light") == "$9.99"
    assert overview_page.get_item_total_price() == "Item total: $39.98"
    assert overview_page.get_tax() == "Tax: $3.20"
    assert overview_page.get_total_price_with_tax() == "Total: $43.18"


def test_order_checkout_completion(added_products):
    """Check that order checkout process finalized and successful order creation message is displayed"""
    checkout_page = added_products.checkout()
    overview_page = checkout_page.fill_in_submit_checkout_form(FIRST_NAME, LAST_NAME, ZIP_POSTAL_CODE)
    checkout_items = overview_page.get_items_in_checkout()

    assert checkout_items == ["Sauce Labs Backpack", "Sauce Labs Bike Light"]

    complete_page = overview_page.finish_checkout()
    checkout_message = complete_page.get_confirmation_message()

    assert checkout_message == "Thank you for your order!"


def test_redirection_to_main_page_after_checkout(added_products):
    """Check that after checkout process finalized user can be redirected to main products page"""
    checkout_page = added_products.checkout()
    overview_page = checkout_page.fill_in_submit_checkout_form(FIRST_NAME, LAST_NAME, ZIP_POSTAL_CODE)
    complete_page = overview_page.finish_checkout()
    product_page = complete_page.get_back_to_product_page()

    assert product_page.get_section_title() == "Products"
