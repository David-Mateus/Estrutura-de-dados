"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
append - Adiciona um item ao final
insert - Adiciona um item no indice escolhido
pop    - Remove do final ou do indice escolhido
del    - apaga um indice
clear  - limpa a lista
extend - estende a lista
"""
# --------+01234
# ------- -54321

string = 'ABCDE'

lista = [123, True, "David", 1.2,[1,23]]
del lista[2] 
lista.append(50) 
lista.pop() 
lista.remove(123)
lista.insert(0, 5)
print(lista)
"""
Cuidados com dados mutaveis
= - copiado o valor (imutaveis)
= - aponta para o mesmo valor na memoria(mutavel)
"""
