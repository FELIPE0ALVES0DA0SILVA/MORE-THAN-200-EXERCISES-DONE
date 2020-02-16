# def hallo_func(greeting, name="You"):
#     return f"{greeting}, {name} Function."


# print(hallo_func("Hi", "Korean"))


def student_info(*args, **kwargs):
    """
    Ask two arguments with different properties, the one with one star give you the values that do not were passed with a variable,
    and the other with two stars give you the values passed with a variable.
    """
    print(args)
    print(kwargs)


courses = ("Math", "Art")
dic = {"name": "John", "age": 22}

student_info(*courses, **dic)

