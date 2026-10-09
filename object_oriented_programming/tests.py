from object_oriented_programming.task3 import Company, HourlyEmployee, SalariedEmployee, Domain

def test_several_companies_created():
    company_1 = Company("Blue Print", Domain.HEALTHCARE)
    company_2 = Company("CapgemCom", Domain.TECHNOLOGY)

    assert company_1.name == "Blue Print"
    assert company_1.domain.value == "HEALTHCARE"
    assert company_2.name == "CapgemCom"
    assert company_2.domain.value == "TECHNOLOGY"


def test_create_several_employees():
    empl_salary_1 = SalariedEmployee("Alice", _salary=4500)
    empl_salary_2 = SalariedEmployee("John", _salary=2300)

    empl_hourly_1 = HourlyEmployee("Kevin", _hourly_rate=80)
    empl_hourly_2 = HourlyEmployee("Anna", _hourly_rate=100)

    assert empl_salary_1.name == "Alice"
    assert empl_salary_1.salary == 4500
    assert empl_salary_1.emp_id == "E1"

    assert empl_salary_2.name == "John"
    assert empl_salary_2.salary == 2300
    assert empl_salary_2.emp_id == "E2"

    assert empl_hourly_1.name == "Kevin"
    assert empl_hourly_1.hourly_rate == 80
    assert empl_hourly_1.emp_id == "E3"

    assert empl_hourly_2.name == "Anna"
    assert empl_hourly_2.hourly_rate == 100
    assert empl_hourly_2.emp_id == "E4"

def test_hire_salaried_employees_into_company(company_1, alice, anna):
    result_alice = company_1.hire(alice)
    result_anna = company_1.hire(anna)
    empl_ids = [emp.emp_id for emp in company_1.employees]

    assert result_alice == "Alice is successfully hired"
    assert result_anna == "Anna is successfully hired"
    assert alice.emp_id in empl_ids
    assert anna.emp_id in empl_ids
    assert len(company_1.employees) == 2
    assert len(empl_ids) == len(set(empl_ids))
    assert alice.company is company_1
    assert anna.company is company_1


def test_hire_employees_into_company(company_2, kevin, barbara, anna):
    company_2.hire(anna)
    result_kevin = company_2.hire(kevin)
    result_barbara = company_2.hire(barbara)
    empl_ids = [emp.emp_id for emp in company_2.employees]

    assert result_kevin == "Kevin is successfully hired"
    assert result_barbara == "Barbara is successfully hired"
    assert anna.emp_id in empl_ids
    assert kevin.emp_id in empl_ids
    assert barbara.emp_id in empl_ids
    assert len(empl_ids) == len(set(empl_ids))
    assert len(company_2.employees) == 3
    assert kevin.company is company_2
    assert barbara.company is company_2
    assert anna.company is company_2


def test_hire_same_employee_twice(company_1, anna):
    result = company_1.hire(anna)
    assert result == "Anna is successfully hired"

    result_2 = company_1.hire(anna)
    assert result_2 == "Anna is already employed by Blue Print company"
    assert len(company_1.employees) == 1


def test_hire_same_employee_into_2_companies(company_1, company_2, anna):
    result_company_1 = company_1.hire(anna)
    result_company_2 = company_2.hire(anna)

    assert result_company_1 == "Anna is successfully hired"
    assert result_company_2 == "Anna is already employed by Blue Print company"

    assert len(company_1.employees) == 1
    assert len(company_2.employees) == 0


def test_fire_employees(company_with_staff, kevin):
    count_before = len(company_with_staff.employees)
    fired_result = company_with_staff.fire(kevin)

    assert fired_result == "Kevin is fired"
    assert kevin not in company_with_staff.employees
    assert kevin.company is None
    assert len(company_with_staff.employees) == count_before - 1


def test_fire_not_employed_employee(company_with_staff, alice):
    count_before = len(company_with_staff.employees)
    fired_result = company_with_staff.fire(alice)

    assert fired_result == "Alice does NOT work at Blue Print"
    assert len(company_with_staff.employees) == count_before


def test_set_get_salary_for_salaried_empl(alice, anna):
    alice.salary = 1000

    assert alice.salary == 1000
    assert anna.salary == 8000


def test_set_get_hourly_pay_empl(kevin, barbara):
    kevin.hourly_rate = 100

    assert kevin.hourly_rate == 100
    assert barbara.hourly_rate == 20


def test_calculate_payment_salaried_empl(alice, anna):
    alice.salary = 5000
    calculation_result_alice = alice.calculate_payment()
    calculation_result_anna = anna.calculate_payment()

    assert calculation_result_alice == 1250
    assert calculation_result_anna == 2000


def test_calculate_payment_hourly_empl(kevin, barbara):
    kevin.hourly_rate = 80
    calculation_result_kevin = kevin.calculate_payment()
    calculation_result_barbara = barbara.calculate_payment()

    assert calculation_result_kevin == 3200
    assert calculation_result_barbara == 800


def test_increase_salary_hourly_rate(company_with_staff, anna, kevin, barbara, alice):
    company_with_staff.raise_pay(anna, 1000)
    company_with_staff.raise_pay(kevin, 50)
    company_with_staff.raise_pay(barbara, 80)
    result_alice = company_with_staff.raise_pay(alice, 1000)

    assert anna.salary == 9000
    assert kevin.hourly_rate == 50
    assert barbara.hourly_rate == 100
    assert result_alice == "Alice does NOT work at Blue Print"


def test_negative_increase_salary_hourly_rate(company_with_staff, anna, barbara):
    increase_salary_anna = company_with_staff.raise_pay(anna, -1000)
    increase_hourly_pay_barbara = company_with_staff.raise_pay(barbara, -8)

    assert increase_salary_anna == "-1000 raise pay value cannot be negative"
    assert anna.salary == 8000
    assert increase_hourly_pay_barbara == "-8 raise pay value cannot be negative"
    assert barbara.hourly_rate == 20


def test_leave_company_by_employee(company_with_staff, alice, barbara):
    result_before = len(company_with_staff.employees)
    result_barbara = barbara.leave_company()
    result_alice = alice.leave_company()

    assert result_barbara == "Barbara is left the company"
    assert barbara.company is None
    assert barbara not in company_with_staff.employees
    assert len(company_with_staff.employees) == result_before - 1
    assert result_alice == "Alice is NOT currently employed"


def test_company_representation(company_with_staff):
    representation = company_with_staff.__repr__()

    assert representation == "Company(Blue Print, HEALTHCARE, Employees:3)"
