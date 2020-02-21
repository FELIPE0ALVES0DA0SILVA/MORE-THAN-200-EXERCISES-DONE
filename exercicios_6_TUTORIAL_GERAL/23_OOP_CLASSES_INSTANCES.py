#  Python Objected-Oriented Programming


class Employee:
    # Class variables
    raise_amount = 1.04

    # __init__ method or constructor
    def __init__(self, first, last, pay):
        # instances variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@ALVESINVESTIMENT.com"

    # Class method
    def fullname(self):
        return f"{self.first} {self.last}"

    # Class method or instance
    def apply_raises(self):
        self.pay = int(self.pay * self.raise_amount)

    # classmethod are used to change all the values of a class, not just within a instance
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amt = amount

    # staticmethod it don't need to pass a first argument how a instance, is just the arguments required to run the function adequated.
    @staticmethod
    def static_is_worlk(day):
        if day.weekday() == 6 or day.weekday() == 7:
            return False
        return True


# employee_1 = Employee("Felipe", "Alves", 350000)
# employee_2 = Employee("Ludmila", "Alves", 70000)

# employee_2.set_raise_amount(1.1)
# print(Employee.__dict__)
# print(employee_1.raise_amt)
# print(employee_2.raise_amt)

import datetime

day = datetime.date(2020, 2, 23)
print(Employee.static_is_worlk(day))
