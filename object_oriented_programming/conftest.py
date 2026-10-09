import pytest


from object_oriented_programming.task3 import Company, Domain, SalariedEmployee, HourlyEmployee, Employee


@pytest.fixture
def company_1():
    return Company("Blue Print", Domain.HEALTHCARE)

@pytest.fixture
def company_2():
    return Company("CapgemCom", Domain.TECHNOLOGY)

@pytest.fixture
def alice():
    return SalariedEmployee("Alice")

@pytest.fixture
def anna():
    return SalariedEmployee("Anna", _salary=8000)

@pytest.fixture
def kevin():
    return HourlyEmployee("Kevin")

@pytest.fixture
def barbara():
    return HourlyEmployee("Barbara", _hourly_rate=20)

@pytest.fixture
def company_with_staff(company_1, anna, kevin, barbara):
    company_1.hire(anna)
    company_1.hire(kevin)
    company_1.hire(barbara)
    return company_1

@pytest.fixture(autouse=True)
def reset_employee_assigned_id_to_0():
    Employee._last_assigned_id = 0
    yield
    Employee._last_assigned_id = 0
