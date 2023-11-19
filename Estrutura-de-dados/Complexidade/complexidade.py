# def inverter_lista(lista, n):
#     tamanho = len(lista)
#     limite = tamanho//2
#     for i in range(limite):
#         aux = lista[i]
#         lista[i] = lista[n-i]
#         lista[tamanho-i] = aux

# 4 + N complexidade de espaço
# 2 + 2*N - complexidade de tempo = O(n)

def temp_duplicados(lista):
    for i in range(len(lista) -1):
        for j in range(i+1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False

print(temp_duplicados('Abacaxi'))