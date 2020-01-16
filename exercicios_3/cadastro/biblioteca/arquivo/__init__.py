from exercicios_3.cadastro.biblioteca.interface import *


def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve algum erro na criação do arquivo')
    else:
        print('Arquivo {} criado com sucesso.'.format(nome))


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print('{:<30}{:>3} anos'.format(dado[0], dado[1]))
    finally:
        a.close()


def cadastrar(arq, nome = 'desconhecido', idade = 0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write('{};{}\n'.format(nome, idade))
        except:
            print('HOUVE UM ERRO NA HORA DE ESCREVER OS DADOS')
        else:
            print('Novo registro de {} adicionado'.format(nome))
            a.close()