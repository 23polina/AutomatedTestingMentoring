import time

import pytest


from pytest_module.solution import ECommerceApp


@pytest.fixture()
def registered_user():
    app = ECommerceApp()
    app.register_user("Kate", "Password123")
    return app


@pytest.fixture()
def user_with_items_in_cart(registered_user):
    registered_user.add_to_cart("Kate", "apple", 5)
    registered_user.add_to_cart("Kate", "banana", 2)
    registered_user.add_to_cart("Kate", "orange", 3)
    return registered_user



def pytest_runtest_setup(item):
    item.start_time = time.time()


def pytest_runtest_teardown(item):
    if hasattr(item, "start_time"):
        item.time_execution = time.time() - item.start_time
        print(f"{item.name} executed for {item.time_execution:.3f} sec")

