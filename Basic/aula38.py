"""
for in com listas
"""
# lista = ['David', 'Mateus', 'Leite']
# count = 0
# for i in lista:
#     print(count, i)
#     count+=1

#Range gera numeros
lista = ['David', 'Mateus', 'Leite']
index = range(len(lista)) # range é faixa(0, 3)
print(index)
for i in range(len(lista)):
    print(i, lista[i])
    