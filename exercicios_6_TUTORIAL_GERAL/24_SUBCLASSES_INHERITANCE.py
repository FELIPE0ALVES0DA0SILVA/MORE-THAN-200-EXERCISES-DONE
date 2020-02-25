# Subclasses - inheritance


class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@email.com"

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.2

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print(f"--->  {emp.fullname()}")


dev_1 = Developer("Felipe", "Alves", 40000, "Python")
dev_2 = Developer("Corey", "Schafer", 50000, "Javascript")
dev_3 = Employee("Test", "User", 60000)

mgr_1 = Manager("Sue", "Smith", 90000, [dev_1, dev_2, dev_3])
print(mgr_1.fullname())
print(mgr_1.employees)

# print(dev_1.prog_lang)
# print(dev_2.prog_lang)
# print(dev_3.raise_amt)
