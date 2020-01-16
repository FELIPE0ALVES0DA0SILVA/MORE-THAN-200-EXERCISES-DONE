# Make a program that read the weight of five peoples. In the end, show what was the major and minor weight readied.

# CREATE A LIST
# MAKE A FOR LOOP OF 1 TO 6 AND 1 BY 1:
#               CREATE A VARIABLE THE CONTAIN THE WEIGHT
#               SAVE THE VARIABLE IN EACH LOOP IN THE LIST
# PRINT THE MAJOR AND MINOR WEIGHT THROUGHOUT THE LIST

saved = []
for c in range(1, 6):
    w = float(input('What is the {}° weight? '.format(c)))
    saved.append(w)
print('The major weight in this list was {:.2f} and the minor was {:.2f}.'.format(max(sorted(saved)), min(sorted(saved))))
