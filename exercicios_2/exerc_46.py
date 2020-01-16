
# Make a program that show in the screen a countdown to the fireworks burst. Going from 10 until 0, with a pause of one second between them.

# IMPORT THE LIBRARY TIME
# USING THE LOOP FOR TO COUNT IN REVERSE OF 0 TO 10 BY 1 IN 1:
#           IMPORT SLEEP METHOD WITH 1 SECOND
#           PRINT TEH NUBER SHOW IN THE LOOP
# PRINT A EXPLOSING

from time import sleep

for c in range(10, - 1, -1):
    sleep(1)
    print(c)
sleep(1)
print('BOOOOOW !!!!!!')
