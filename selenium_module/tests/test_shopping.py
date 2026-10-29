def test_add_items_into_cart(login_into_swag_labs, navigator):
    """Check that items are added with correct price into cart and displayed there"""
    login_into_swag_labs.add_item_to_cart("Sauce Labs Bike Light")
    login_into_swag_labs.add_item_to_cart("Sauce Labs Bolt T-Shirt")
    cart_items_amount = login_into_swag_labs.get_cart_amount()
    login_into_swag_labs.go_to_cart()
    cart_page = navigator.cart_page()

    assert cart_items_amount == 2
    assert cart_page.get_items_in_cart() == ["Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt"]
    assert cart_page.get_price("Sauce Labs Bike Light") == "$9.99"
    assert cart_page.get_price("Sauce Labs Bolt T-Shirt") == "$15.99"


def test_remove_items_from_cart(login_into_swag_labs, navigator):
    """Check that items in cart can be removed from cart on SwagLabs page"""
    login_into_swag_labs.add_item_to_cart("Sauce Labs Bike Light")
    login_into_swag_labs.add_item_to_cart("Sauce Labs Bolt T-Shirt")
    login_into_swag_labs.remove_item_from_cart("Sauce Labs Bike Light")
    cart_items_amount_after_removing = login_into_swag_labs.get_cart_amount()
    login_into_swag_labs.go_to_cart()
    cart_page = navigator.cart_page()

    assert cart_items_amount_after_removing == 1
    assert cart_page.get_items_in_cart() == ["Sauce Labs Bolt T-Shirt"]
