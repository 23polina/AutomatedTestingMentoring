def test_delete_item_from_cart(added_products):
    """Check that items in cart can be removed from cart on cart page"""
    assert added_products.get_items_in_cart() == ["Sauce Labs Backpack", "Sauce Labs Bike Light"]

    added_products.remove_item_from_cart_page("Sauce Labs Backpack")

    assert added_products.get_items_in_cart() == ["Sauce Labs Bike Light"]


def test_state_of_deleted_product(added_products, navigator):
    """Check button state for an item in cart and removed item from cart"""
    added_products.remove_item_from_cart_page("Sauce Labs Backpack")
    added_products.continue_shopping()
    products_page = navigator.products_page()

    assert products_page.get_button_text("Sauce Labs Backpack") == "Add to cart"
    assert products_page.get_button_text("Sauce Labs Bike Light") == "Remove"
