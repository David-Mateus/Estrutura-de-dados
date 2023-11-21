# lista linear em alocação sequencial
lista = [5, 8, 2, 7, 0]
# acesso aleatório
# print(lista[3])

# Buscar em lista
def busca(lista, elem):
    
    for i in range(len(lista)):
        if(lista[i] == elem):
            return i
        return None

print(busca([1,2,3,4], 2))