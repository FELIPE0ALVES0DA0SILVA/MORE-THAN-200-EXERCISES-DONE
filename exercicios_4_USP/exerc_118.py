# Make a ath board that go until 10 X 10 and start from 1 X 1 bidirectional.

linha = 0
coluna = 0
while linha <= 10:
    while coluna <= 10:
        print(linha * coluna, end='\t')
        coluna += 1
    linha += 1
    print()
    coluna = 1