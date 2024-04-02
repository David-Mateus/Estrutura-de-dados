"""
Split e join com list e str
split - divide uma string - retorna uma lista
join - une uma string
"""

frase = 'Olha só que, coisa interessante'
lista_palavras = frase.split("")
print(lista_palavras)

frase = 'Olha só que, coisa interessante'
lista_palavras = frase.split(',')
print(lista_palavras)

#Alterar o valor
for i, frase in enumerate(lista_palavras):
    #Valor antigo ou 0 = Novo valor
    lista_palavras[i] = lista_palavras[i].strip()
# strip()  -> corta espaço do inicio e no fim
# rstrip() -> corta da direita
# lstrip() -> corta da esquerda

frase = input().split()
var1 = frase[0]
var2 = frase[1]
var3 = frase[2]

print(sum)

# frase_unidas = 'como vai ser a junção'.join(passarInteravel), so pode list, string e tuplas