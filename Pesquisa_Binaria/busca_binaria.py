def busca_binaria(lista, item):
    baixo = 0
    alto = len(lista)-1

    while baixo <= alto:

        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None



b =  busca_binaria([1,2,3,4,5], 3)
print(b)
