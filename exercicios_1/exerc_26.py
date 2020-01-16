# CREATE THE VARIABLE THE WILL CONTAIN THE PHRASE ENTERED BY THE USER
# UPPERCASE THE PHRASE
# STRIPPED THE PHRASE
# COUNT THE ' A ' IN THE PHRASE
# SHOW THE POSITION OF THE FIRST ' A ' FIND OUT IN THE PHRASE
# SSHOW THE POSITION OF THE FIRST ' A ' FIND OUT IN THE PHRASE, STARTING OF THE RIGHT SIDE TO THE LEFT SIDE.
# PRINT THE POSITIONS FINDS IN THE TWO CASES.

phrase = str(input('Enter any phrase: '))


# Letras maiúsculas e remoção dos espaços no comço e fim da frase
uppercase = phrase.upper()
strip = uppercase.strip()

# Contagem dos As pedidos
times_count = uppercase.count('A')

# Posição do primeiro A
position_find = uppercase.find('A')

# Juntamento da frase e posição do último A
join1 = ''.join(uppercase)
position_end = join1.rfind('A')

print('The letter A show up  {} times'
       '\nThe letter A showed up in the {} position'
       '\nThe last letter A showed up in the {} position'
       '.'.format(times_count, position_find, position_end))
