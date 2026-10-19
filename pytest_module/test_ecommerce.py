import pytest


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("username, password",
                         [
                             ("Palina", "Password1"),
                             ("Karina", "Password2"),
                             ("Anna", "Password3")
                         ])
def test_successful_user_registration(ecommerce_app, username, password):
    """Check successful user registration and user storage in users list"""
    result_user_registration = ecommerce_app.register_user(username, password)

    assert result_user_registration is True
    assert ecommerce_app.users == {username: password}


@pytest.mark.regression
def test_register_same_user_twice(ecommerce_app):
    """Check that the user cannot be registered twice"""
    successful_result_registration = ecommerce_app.register_user("Anna", "Password2")
    twice_registration_result = ecommerce_app.register_user("Anna", "Password2")

    assert successful_result_registration is True
    assert twice_registration_result is False
    assert ecommerce_app.users == {"Anna": "Password2"}


@pytest.mark.xfail(reason="Feature under development", strict=True)
@pytest.mark.parametrize("username, password, expected_error_message",
                         [
                             ("", "Password1", "Username cannot be empty"),
                             ("User1", "", "Password cannot be empty"),
                             (None, "Password", "Username cannot be empty")
                         ])
def test_unsuccessful_registration(ecommerce_app, username, password, expected_error_message):
    """Check that registration fails with an error message if username or password is empty or None"""
    registration_result = ecommerce_app.register_user(username, password)

    assert registration_result == expected_error_message


@pytest.mark.smoke
@pytest.mark.regression
def test_listing_products(ecommerce_app):
    """Check expected listed products"""
    product = ecommerce_app.list_products()

    assert product == {'apple': 1.0, 'banana': 0.5, 'orange': 0.75}


@pytest.mark.smoke
@pytest.mark.regression
def test_successful_add_to_cart(registered_user):
    """Check that several different products added to the cart are stored with their own amounts"""
    result_adding_banana = registered_user.add_to_cart("Kate", "banana", 2)
    result_adding_orange = registered_user.add_to_cart("Kate", "orange", 3)
    result_adding_apple_1 = registered_user.add_to_cart("Kate", "apple", 5)
    result_adding_apple_2 = registered_user.add_to_cart("Kate", "apple", 10)

    assert result_adding_banana == True
    assert result_adding_orange == True
    assert result_adding_apple_1 == True
    assert result_adding_apple_2 == True
    assert registered_user.cart == {"apple": 15,
                                    "orange": 3,
                                    "banana": 2}


@pytest.mark.regression
@pytest.mark.parametrize("username, product, amount",
                         [("Kate", "milk", 2),
                          ("Palina", "apple", 4)])
def test_unsuccessful_add_to_cart(registered_user, username, product, amount):
    """Check that product adding to the cart fails for an unregistered user or an unknown product"""
    result = registered_user.add_to_cart(username, product, amount)

    assert result is False
    assert registered_user.cart == {}


@pytest.mark.skip(reason="Feature hasn't implemented yet")
@pytest.mark.parametrize("username, product, amount",
                         [
                             ("Kate", "", 2),
                             ("Kate", None, 4)
                         ])
def test_add_not_specified_product_to_cart(registered_user, username, product, amount):
    """Check that a product with an empty or None name cannot be added to the cart"""
    result = registered_user.add_to_cart(username, product, amount)

    assert result == "Product is NOT specified. Select a product"


@pytest.mark.smoke
@pytest.mark.regression
def test_checkout(app_with_items_in_cart):
    """Check that checkout returns the total price of all cart products and empties the cart"""
    assert app_with_items_in_cart.cart == {"apple": 5,
                                            "banana": 2,
                                            "orange": 3}
    total_amount = app_with_items_in_cart.checkout()

    assert total_amount == 8.25
    assert app_with_items_in_cart.cart == {}


@pytest.mark.xfail(reason="Feature under development", strict=True)
def test_empty_cart_checkout(registered_user):
    """Check that checkout cannot be done for empty cart"""
    result = registered_user.checkout()

    assert result == "The user has empty cart"


@pytest.mark.xfail(reason="Feature under development", strict=True)
def test_not_registered_user_cart_checkout(ecommerce_app):
    """Check that an unregistered user cannot check out."""
    result = ecommerce_app.checkout()

    assert result == "The user does NOT registered"
