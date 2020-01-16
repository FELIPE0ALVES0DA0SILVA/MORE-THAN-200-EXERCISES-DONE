# Create a little system modularized that allow you sign up peoples for your name and age in a file of simple text.
# O system will only have two opptions:
# Sign up a new person and list all the persons signed up.

from time import sleep
from exercicios_3.cadastro.biblioteca.arquivo import *

arq = 'Cursoemvideo.txt'
if not arquivoexiste(arq):
    criararquivo(arq)
while True:
    respostas = menu(['VER PESSOAS CADASTRADAS', 'CADASTRAR NOVA PESSOA', 'SAIR DO SISTEMA'])
    if respostas == 1:
        lerarquivo(arq)
    elif respostas == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif respostas == 3:
        cabecalho('SAINDO DO SISTEMA ATÉ LOGO!')
        break
    else:
        print('\033[31mErro: digite uma opção válida\033[m')
        sleep(2)

