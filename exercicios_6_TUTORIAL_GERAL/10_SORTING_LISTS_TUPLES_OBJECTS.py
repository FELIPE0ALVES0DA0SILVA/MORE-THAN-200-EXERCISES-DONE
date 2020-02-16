my_list = [
    899,
    -317,
    -543,
    -196,
    -222,
    887,
    459,
    380,
    -305,
    -782,
    -45,
    352,
    849,
    -17,
    312,
    522,
]
# my_list.sort(reverse=True)
# print(sorted(my_list, key=abs))

my_tuple = (
    899,
    -317,
    -543,
    -196,
    -222,
    887,
    459,
    380,
    -305,
    -782,
    -45,
    352,
    849,
    -17,
    312,
    522,
)

# print(sorted(my_tuple))
# print(my_tuple)


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"{self.name}, {self.age}, ${self.salary}"


e1 = Employee("Carl", 37, 70000)
e2 = Employee("Sarah", 29, 80000)
e3 = Employee("John", 43, 90000)
employees = [e1, e2, e3]


def sorti(emp):
    return emp.salary


print(sorted(employees, key=lambda e: e.age))
