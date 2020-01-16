
# write a program that read two integers numbers and compared themselves, showing
# in the screen a menssage:
#    -- The first value is more large than the second.
#    -- The second value is more large than the first.
#    -- Do note exist more large value between them. Both is equals.

#   import the library to do the program wait some seconds to run, after the inputs
#   Create the variables that will contain the value throughout the inputs
#   create the method that will run the wait of the program after the inputs variables run
#   Create the IF ELIF to choice the answers
#        Print the answers of each IF ELIF created



import time
value_one = float(input('Enter the first value: '))
value_two = float(input('Enter the second value: '))
print()
print()

time.sleep(2)

if value_one > value_two:
    print('The first value is the largest.')
elif value_two > value_one:
    print('The second value is the largest.')
elif value_one == value_two:
    print('The two values have the same wighted, they are equivalent.')
