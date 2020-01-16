# Write the function n_primos that receive how an argument a integer number major or equal
# to two like a parameter and turn off the amount of prime numbers that
# exist between two and n (including two and, if be the case, N).


def n_primos(valor):
    total = 0
    if valor == 2:
        total +=1
    else:
        for contador in range(2, valor):
            primo = True

            for contagem in range(2, contador):
                if contador % contagem == 0:
                    primo = False
            if primo:
                total += 1
    return total
