import time
import pytest
from pytest_module.solution import ECommerceApp

@pytest.fixture()
def ecommerce_app():
    """Return a clean ECommerceApp instance with no users and an empty cart"""
    return ECommerceApp()

@pytest.fixture()
def registered_user():
    """Return an ECommerceApp instance with the user 'Kate' already registered"""
    app = ECommerceApp()
    app.register_user("Kate", "Password123")
    return app


@pytest.fixture()
def app_with_items_in_cart(registered_user):
    """Return an ECommerceApp instance with the user 'Kate' and added products in cart"""
    registered_user.add_to_cart("Kate", "apple", 5)
    registered_user.add_to_cart("Kate", "banana", 2)
    registered_user.add_to_cart("Kate", "orange", 3)
    return registered_user


def pytest_runtest_setup(item):
    """Hook: runs before each test and stores the start time on the test item.
    The saved time is read in pytest_runtest_teardown to calculate how long
    the test took"""
    item.start_time = time.time()


def pytest_runtest_teardown(item):
    """Hook: runs after each test and prints how long the test took"""
    if hasattr(item, "start_time"):
        item.time_execution = time.time() - item.start_time
        print(f" {item.name} executed for {item.time_execution:.3f} sec")
