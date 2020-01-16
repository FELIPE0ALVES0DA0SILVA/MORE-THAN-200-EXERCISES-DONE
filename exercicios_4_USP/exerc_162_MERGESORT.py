def MERGE_SORT_rescursivo(lista):
    if len(lista) <= 1:     # BASE DA RECURSÃO
        return lista
    meio = len(lista) // 2

    lado_esquerdo = MERGE_SORT_rescursivo(lista[:meio])
    lado_direito = MERGE_SORT_rescursivo(lista[meio:])

    return MERGE(lado_esquerdo, lado_direito)


def MERGE(lado_esquerdo, lado_direito):
    if not lado_esquerdo:     #
        return lado_direito   # OUTRA BASE RECURSIVA
    elif not lado_direito:    #
        return lado_esquerdo  #
    if lado_esquerdo[0] < lado_direito[0]:
        return [lado_esquerdo[0]] + MERGE(lado_esquerdo[1:], lado_direito)
    else:
        return [lado_direito[0]] + MERGE(lado_esquerdo, lado_direito[1:])
