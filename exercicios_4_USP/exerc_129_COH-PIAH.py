import re


def tratar_erro_float(valor):
    while True:
        valores = []
        valores_alterado = []
        valor_principal = input(valor)
        valores.append(valor_principal)
        for item in valores:
            for itens in item:
                valores_alterado.append(itens)
        for itens, value in enumerate(valores_alterado):
            if value == ',':
                valores_alterado[itens] = '.'
        valor_principal = ''
        for value in valores_alterado:
            valor_principal += value
        try:
            valor_principal = float(valor_principal)
        except:
            print('Valor digitado inválido! Digite novamente.')
        else:
            return valor_principal


def le_assinatura():
    '''
    A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos
    '''
    print('Bem-vindo ao detector automático de COH-PIAH.')
    print()
    print()
    tamanho_medio_palavra = tratar_erro_float("Entre o tamanho medio de palavra:")
    type_token = tratar_erro_float("Entre a relação Type-Token:")
    razao_hapax = tratar_erro_float("Entre a Razão Hapax Legomana:")
    tamanho_medio_sentanca = tratar_erro_float("Entre o tamanho médio de sentença:")
    complex_media_sentenca = tratar_erro_float("Entre a complexidade média da sentença:")
    tamanho_medio_frase = tratar_erro_float("Entre o tamanho medio de frase:")
    return [tamanho_medio_palavra, type_token, razao_hapax, tamanho_medio_sentanca,  complex_media_sentenca, tamanho_medio_frase]


def le_textos():
    textos = []
    iterar = 1
    while True:
        texto = str(input('Digite o texto {} (aperte enter para sair):'.format(iterar))).strip()
        if texto == '':
            break
        textos.append(texto)
        iterar += 1
    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = []
    for string in texto:
        separar = re.split(r'[.!?]+', string)
        if separar[-1] == '':
            del separar[-1]
        sentencas.append(separar[:])
        separar.clear()
    return sentencas


def media_sentenca(ler_textos):
    sentencas = separa_sentencas(ler_textos)
    c = s = 0
    media = []
    for listas in sentencas:
        for sente in listas:
            s += 1
            for unidade in sente:
                c += 1
        m = c / s
        media.append(m)
        c = s = 0
    return media


def complex_sentenca_media_frase(ler_textos):
    frases = separa_frases(ler_textos)
    sentences = separa_sentencas(ler_textos)
    media_sentenca = []
    media_frase = []
    complexidade = []
    f = s = 0
    for lotes in frases:
        for lote in lotes:
            f += 1
        media_frase.append(f)
        f = 0
    for lotes in sentences:
        for lote in lotes:
            s += 1
        media_sentenca.append(s)
        s = 0
    for posicao, valor in enumerate(media_frase):
        for lugar, item in enumerate(media_sentenca):
            if posicao == lugar:
                media = valor / item
                complexidade.append(media)
    return complexidade


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    sentencas = separa_sentencas(sentenca)
    frases = []
    precisa = []
    definitiva = []
    for lista in sentencas:
        for oracao in lista:
            separar = re.split(r'[,:;]+', oracao)
            frases.append(separar[:])
            separar.clear()
        precisa.append(frases[:])
        frases.clear()
    for lote in precisa:
        for lista in lote:
            for cada in lista:
                frases.append(cada)
        definitiva.append(frases[:])
        frases.clear()
    return definitiva


def media_frase(ler_textos):
    frase = separa_frases(ler_textos)
    c = f = 0
    media = []
    for listas in frase:
        for fra in listas:
            f += 1
            for unidade in fra:
                c += 1
        m = c / f
        media.append(m)
        c = f = 0
    return media


def separa_palavras(valor):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    frases = separa_frases(valor)
    palavras = []
    resultado = []
    conclusao = []
    for lista in frases:
        for cada in lista:
            separar = cada.split()
            palavras.append(separar[:])
            separar.clear()
        resultado.append(palavras[:])
        palavras.clear()
    for lote in resultado:
        for lista in lote:
            for cada in lista:
                palavras.append(cada)
        conclusao.append(palavras[:])
        palavras.clear()
    return conclusao


def media_palavras(lista_palavras):
    p = c = 0
    lista_palavra = separa_palavras(lista_palavras)
    resultado = []
    for listas in lista_palavra:
        for palavra in listas:
            p += 1
            for unidade in palavra:
                c += 1
        m = c / p
        resultado.append(m)
        c = p = 0
    return resultado


def n_palavras_unicas(valor):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de de palavras que aparecem uma unica vez'''
    lista_palavra = separa_palavras(valor)
    conclusao = []
    frequencia = 0
    for lista in lista_palavra:
        for palavra in lista:
            resultado = lista.count(palavra)
            if resultado == 1:
                frequencia += 1
        conclusao.append(frequencia)
        frequencia = 0
    return conclusao


def hapax_legomana(valor):
    p_total = 0
    total = separa_palavras(valor)
    unicas = n_palavras_unicas(valor)
    pal_tot = []
    conclusao = []
    for lista in total:
        for contagem in lista:
            p_total += 1
        pal_tot.append(p_total)
        p_total = 0
    for posicao, item in enumerate(unicas):
        for cada, obj in enumerate(pal_tot):
            if posicao == cada:
                media = item / obj
                conclusao.append(media)
    return conclusao


def n_palavras_diferentes(valor):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    lista_palavras = separa_palavras(valor)
    valores = []
    conclusao = []
    frequencia = 0
    for lista in lista_palavras:
        for palavra in lista:
            if palavra not in valores:
                frequencia += 1
                valores.append(palavra)
        conclusao.append(frequencia)
        valores.clear()
        frequencia = 0
    return conclusao


def type_token(valor):
    p_total = 0
    pal_tot = []
    diferentes = n_palavras_diferentes(valor)
    total = separa_palavras(valor)
    conclusao = []
    for lista in total:
        for contagem in lista:
            p_total += 1
        pal_tot.append(p_total)
        p_total = 0
    for posicao, item in enumerate(diferentes):
        for cada, obj in enumerate(pal_tot):
            if posicao == cada:
                media = item / obj
                conclusao.append(media)
    return conclusao


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    resultado = []
    conclusao = []
    palavras = media_palavras(texto)
    type = type_token(texto)
    hapax = hapax_legomana(texto)
    sentenca = media_sentenca(texto)
    complex = complex_sentenca_media_frase(texto)
    frase = media_frase(texto)
    for p, a in enumerate(palavras):
        for t, e in enumerate(type):
            for h, i in enumerate(hapax):
                for s, o in enumerate(sentenca):
                    for c, u in enumerate(complex):
                        for f, ao in enumerate(frase):
                            if p == t == h == s == c == f:
                                resultado.append(a)
                                resultado.append(e)
                                resultado.append(i)
                                resultado.append(o)
                                resultado.append(u)
                                resultado.append(ao)
                                conclusao.append(resultado[:])
                                resultado.clear()
    return conclusao


def calcula_assinaturas(valor):
    return valor


def compara_assinatura(ass_a, ass_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    assinatura_fornecida = ass_a
    if 'a' in ass_b[0][:]:
        assinatura_textos = calcula_assinatura(ass_b)
    else:
        assinatura_textos = []
        assinatura_textos.append(ass_b)
    somatorio = 0
    lista_somatorio = []
    for lista in assinatura_textos:
        for posicao, item in enumerate(lista):
            diferenca = abs(assinatura_fornecida[posicao] - item)
            somatorio += diferenca
        Sab = somatorio / 6
        lista_somatorio.append(Sab)
        somatorio = 0
    return lista_somatorio


def avalia_textos(texto, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    menor = 0
    for posicao, cada in enumerate(ass_cp):
        if min(ass_cp) == cada:
            menor = posicao
            break
    return menor


print(compara_assinatura([4.33, 0.23, 0.14, 13.28, 1.86, 0.0], [4.33, 0.23, 0.14, 13.28, 1.86, 0.0]))
