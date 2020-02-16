courses = ["History", "Math", "Physics", "CompSci"]
courses.append("Art")
courses.insert(1, "Quemistry")
courses_2 = ["Education", "Citizenship"]
courses.extend(
    courses_2
)  # This method make a loop and add all the items of a sublist in the main list
numbers = [1, 2, 3, 4, 5]
numbers.sort(reverse=True)
print(courses)
print(numbers)
courses_str = " - ".join(courses)
print(courses_str)
new_list = courses_str.split(" - ")
print(new_list)
cs_courses = {"History", "Math", "Physics", "CompSci"}
art_courses = {"History", "Math", "Art", "Design"}
print(cs_courses.intersection(art_courses))
