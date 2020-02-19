from collections import namedtuple

Color = namedtuple("Coloe", ["red", "green", "blue"])

color = Color(red=55, green=33, blue=99)

print(color.green)
