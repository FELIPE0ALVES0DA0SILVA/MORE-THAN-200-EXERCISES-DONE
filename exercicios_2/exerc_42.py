
# Remake the challenge 35 of the triangles, increasing the tool to show what type of triangle will be formed.
#           Equilateral
#           Isosceles
#           Escalene

# CREATE THREE FLOAT VARIABLES TAHT WILL READ ONE STRAIGHT VALUE PER EACH VARIABLE
# MAKE THE CALCULUS TO SEE IF WITH THE VALUES IS POSSIBLE FORMER A TRIANGLE
# MAKE ANOTHER CALCULUS TO SEE WEATHER WITH THE  VALUES IS REALLY POSSIBLE TO MAKE A TRIANGLE, SO WHAT KIND OF TRIANGLE IS ,GIVEN THE VALUES
# IF IS NOT POSSIBLE FORMER A TRIANGLE WITH THE VALUES:
#           PRINT THAT IS NOT POSSIBLE FORMER A TRIANGLE WITH THE INFORMED VALUES
# ELSE:
#           IF IS POSSIBLE FORMER A TRIANGLE WITH THE INFORMED VALUES
#                       PRINT THAT IS POSSIBLE FORMER A TRIANGLE WITH THE VALUES
#                       IF THE FORMED TRIANGLE BE A EQUILATERAL TRIANGLE:
#                                   PRINT THAT ITS TRIANGLE IS A EQUILATERAL TRIANGLE
#                       ELIF THE FORMED TRIANGLE BE A ISOSCELES TRIANGLE:
#                                   PRINT THAT ITS FORMED TRIANGLE IS A ISOSCELES
#                       ELIF THE FORMED TRIANGLE BE A SCALENE TRIANGLE:
#                                   PRINT TAHT ITS TRIANGLE IS A SCALENE TRIANGLE

length1 = float(input('Enter the first straight value: '))
length2 = float(input('Enter the second straight value: '))
length3 = float(input('Enter the third straight value: '))

formula_1 = (length1 + length2)
formula_2 = (length2 + length3)
formula_3 = (length1 + length3)

equilateral = length1 == length2 == length3
isosceles = length1 == length2 != length3 or length1 != length2 == length3 or length1 == length3 != length2
escalene = length1 != length2 != length3 and length1 != length3

if formula_1 > length3 or formula_2 > length1 or formula_3 > length2 :
    print('It is possible former a triangle. ', end='')
    if equilateral:
        print('This triangle is equilateral.')
    elif isosceles:
        print('This triangle is isosceles.')
    elif escalene:
        print('This triangle is escalene.')
else:
    print('With the values especified, do not is possible former a triangle.')