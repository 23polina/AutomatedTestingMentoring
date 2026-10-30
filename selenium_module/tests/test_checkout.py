from selenium_module.data.test_data import FIRST_NAME, LAST_NAME, ZIP_POSTAL_CODE


def test_calculation_price_correctness(added_products, navigator):
    """Check that item's price is displayed correctly and total price is calculated correctly during checkout process"""
    added_products.checkout()
    checkout_page = navigator.checkout_page()
    overview_page = checkout_page.fill_in_submit_checkout_form(FIRST_NAME, LAST_NAME, ZIP_POSTAL_CODE)

    assert overview_page.get_price("Sauce Labs Backpack") == "$29.99"
    assert overview_page.get_price("Sauce Labs Bike Light") == "$9.99"
    assert overview_page.get_item_total_price() == "Item total: $39.98"
    assert overview_page.get_tax() == "Tax: $3.20"
    assert overview_page.get_total_price_with_tax() == "Total: $43.18"


def test_order_checkout_completion(added_products, navigator):
    """Check that order checkout process finalized and successful order creation message is displayed"""
    added_products.checkout()
    checkout_page = navigator.checkout_page()
    overview_page = checkout_page.fill_in_submit_checkout_form(FIRST_NAME, LAST_NAME, ZIP_POSTAL_CODE)
    checkout_items = overview_page.get_items_in_checkout()

    assert checkout_items == ["Sauce Labs Backpack", "Sauce Labs Bike Light"]

    overview_page.finish_checkout()
    complete_page = navigator.checkout_complete_page()
    checkout_message = complete_page.get_confirmation_message()

    assert checkout_message == "Thank you for your order!"


def test_redirection_to_main_page_after_checkout(added_products, navigator):
    """Check that after checkout process finalized user can be redirected to main products page"""
    added_products.checkout()
    checkout_page = navigator.checkout_page()
    overview_page = checkout_page.fill_in_submit_checkout_form(FIRST_NAME, LAST_NAME, ZIP_POSTAL_CODE)
    overview_page.finish_checkout()
    complete_page = navigator.checkout_complete_page()
    complete_page.get_back_to_product_page()
    products_page = navigator.products_page()

    assert products_page.get_section_title() == "Products"
