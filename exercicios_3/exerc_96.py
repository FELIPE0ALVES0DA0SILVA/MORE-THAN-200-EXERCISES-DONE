# Make a program that read a function called area(),
# that input the dimension of a rectangular ground(width and length)
# and show the area of the terrain.


def area(width, length):
    a = width * length
    print('A área desse terreno {} X {} é de {} m^2.'.format(width, length, a))


area(width = float(input('LARGURA (m): ')), length = float(input('COMPRIMENTO (m): ')))
