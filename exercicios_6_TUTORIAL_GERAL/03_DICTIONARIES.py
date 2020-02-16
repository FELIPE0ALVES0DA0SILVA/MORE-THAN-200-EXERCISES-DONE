student = {"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
student.update({"name": "Felipe", "phone": "555-5555", "age": 22})
age = student.pop("age")
print(student, age)

for key, value in student.items():
    print(key, value)
