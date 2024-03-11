"""
Introdução ao try/except
try -> tentar
except -> ocorreu algum error
"""

try:
    numero = input('Vou dobrar o número que você digitar: ')
    numero_int = int(numero)
    print(f"O dobro de {numero} é {numero_int * 2}")
except:
    print("Houve um erro de entrada: VOCE DIGITIU UMA PALAVRA OU FLOAT")