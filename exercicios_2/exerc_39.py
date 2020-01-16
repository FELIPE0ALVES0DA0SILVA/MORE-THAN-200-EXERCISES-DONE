
# Make a program that read the year and date of born of a men and inform,
# according with your age:
#    -- If he still go to enlist to the military service.
#    -- If it's time of enlist.
#    -- If already past time of enlistment.

# Your program also will should show the missing time or that passed the deadline.
# Import the specific library: datetime
# Declare the variables of the program
# Create the specific method with your imported library
# Create the IF ELIF existing to put your alternatives
#       Print the results that you desired

from datetime import date

men = str(input('You is a man?')).upper()

if men == 'YES':
    year_born = int(input('What year you is born? '))

    actual = date.today().year   # For take only the current year, let out the day and month respectively
    current_year = actual
    age = current_year - year_born
    months = age*12
    months_service = 18*12

    if year_born <= current_year:
        if age < 18:
            missing_time = months_service - months
            print('You yet have time to enlist yourself, missing {} months to you.'.format(missing_time))
        elif age == 18:
            print('You just in time to enlist yourself in the military service.')
        elif age > 18:
            past_time = -1*(months_service - months)
            print('You already past time to enlist yourself in the military service BOY!'
                  ' Run and sign up as more as faster that you can, already passed {}'
                  ' months to you, boy.'.format(past_time))
    else:
        print('Born first, then you come here to sign up yourself to enlistment.')
elif men == 'NO':
    print('You is a woman, the enlistment is optional.')
else:
    print("Animals don't serve the army.")
