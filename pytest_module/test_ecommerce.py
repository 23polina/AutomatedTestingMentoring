import pytest

from pytest_module.solution import ECommerceApp


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("username, password",
                         [
                             ("Palina", "Password1"),
                             ("Karina", "Password2"),
                             ("Anna", "Password3")
                         ])
def test_successful_user_registration(username, password):
    """Check successful user registration"""
    user = ECommerceApp()
    result_user_registration = user.register_user(username, password)

    assert result_user_registration is True
    assert user.users == {username: password}


@pytest.mark.regression
def test_registrate_same_user_twice():
    """Check that the same user cannot be registered twice"""
    user = ECommerceApp()
    successful_result_registration = user.register_user("Anna", "Password2")
    twice_registration_result = user.register_user("Anna", "Password2")

    assert successful_result_registration is True
    assert twice_registration_result is False
    assert user.users == {"Anna": "Password2"}


@pytest.mark.xfail(reason="Feature under development", strict=True)
@pytest.mark.parametrize("username, password, expected_error_message",
                         [
                             ("", "Password1", "Username cannot be empty"),
                             ("User1", "", "Password cannot be empty"),
                             (None, "Password", "Username cannot be empty")
                         ])
def test_unsuccessful_registration(username, password, expected_error_message):
    """Check unsuccessful registration of the user"""
    user = ECommerceApp()
    registration_result = user.register_user(username, password)

    assert registration_result == expected_error_message


@pytest.mark.smoke
@pytest.mark.regression
def test_listing_products():
    """Check expected listed products"""
    user = ECommerceApp()
    product = user.list_products()

    assert product == {'apple': 1.0, 'banana': 0.5, 'orange': 0.75}


@pytest.mark.smoke
@pytest.mark.regression
def test_successful_add_to_cart(registered_user):
    """Check that products can be successfully added into the cart"""
    registered_user.add_to_cart("Kate", "banana", 2)
    registered_user.add_to_cart("Kate", "orange", 3)
    registered_user.add_to_cart("Kate", "apple", 5)
    registered_user.add_to_cart("Kate", "apple", 10)

    assert registered_user.cart == {"apple": 15,
                                    "orange": 3,
                                    "banana": 2}


@pytest.mark.regression
@pytest.mark.parametrize("username, product, amount",
                         [("Kate", "milk", 2),
                          ("Palina", "apple", 4)])
def test_unsuccessful_add_to_cart(registered_user, username, product, amount):
    """Check negative scenarios for adding products into the cart"""
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
    """Check that products with NOT specified name cannot be added into cart"""
    result = registered_user.add_to_cart(username, product, amount)

    assert result == "Product is NOT specified. Select a product"


@pytest.mark.smoke
@pytest.mark.regression
def test_checkout(user_with_items_in_cart):
    """Check checkout functionality"""
    assert user_with_items_in_cart.cart == {"apple": 5,
                                            "banana": 2,
                                            "orange": 3}

    total_amount = user_with_items_in_cart.checkout()

    assert total_amount == 8.25
    assert user_with_items_in_cart.cart == {}


@pytest.mark.xfail(reason="Feature under development", strict=True)
def test_empty_cart_checkout(registered_user):
    """Check that checkout cannot be done for empty cart"""
    result =  registered_user.checkout()
    assert result == "The user has empty cart"


@pytest.mark.xfail(reason="Feature under development", strict=True)
def test_not_registered_user_cart_checkout():
    """Check that NOT registered user cannot check out"""
    user = ECommerceApp()
    result = user.checkout()

    assert result == "The user does NOT registered"
