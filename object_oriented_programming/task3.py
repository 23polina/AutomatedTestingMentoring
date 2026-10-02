from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import ClassVar

@dataclass
class Employee(ABC):
    name: str
    emp_id: str = None
    _company: str = None
    _last_assigned_id: ClassVar[int] = 0

    def __post_init__(self):
        Employee._last_assigned_id += 1
        self.emp_id = f"E{Employee._last_assigned_id}"

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, company_name):
        self._company = company_name

    def leave_company(self):
        if self.company is not None:
            self.company.fire(self)
            return f"{self.name} is left the company"

        return f"{self.name} is NOT currently employed"


    @abstractmethod
    def calculate_payment(self):
        pass


@dataclass
class HourlyEmployee(Employee):
    _hourly_rate: int = 0

    @property
    def hourly_rate(self):
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, hourly_rate_value):
        self._hourly_rate = hourly_rate_value

    def calculate_payment(self):
        work_week = 40
        payment = work_week * self._hourly_rate
        return payment

@dataclass
class SalariedEmployee(Employee):
    _salary: int = 0

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary_value):
        self._salary = salary_value

    def calculate_payment(self):
        payment_weekly = self._salary / 4
        return payment_weekly



class Domain(Enum):
    TECHNOLOGY = "TECHNOLOGY"
    HEALTHCARE = "HEALTHCARE"
    RETAIL = "RETAIL"


@dataclass
class Company:
    name:str
    domain: Domain
    employees: list = field(default_factory=list)


    def hire(self, employee):
        if employee.company is None and employee not in self.employees:
            self.employees.append(employee)
            employee.company = self
            return f"{employee.name} is successfully hired"
        else:
            return f"{employee.name} is already employed by {employee.company.name} company"

    def fire(self, employee):
        if employee.company is self:
            self.employees.remove(employee)
            employee.company = None
            return f"{employee.name} is fired"
        else:
            return f"{employee.name} does NOT work at {self.name}"


    def raise_pay(self, employee, raise_value):
        if employee.company is self:
            if isinstance(employee, HourlyEmployee):
                employee.hourly_rate += raise_value
                return f"{employee.name} has {employee.hourly_rate} hourly rate"
            elif isinstance(employee, SalariedEmployee):
                employee.salary += raise_value
                return f"{employee.name} has {employee.salary} salary"
        else:
            return f"{employee.name} does NOT work at {self.name}"

    def __repr__(self):
        return f"Company({self.name}, {self.domain.name}, Employees:{len(self.employees)})"
