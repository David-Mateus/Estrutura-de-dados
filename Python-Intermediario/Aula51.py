"""
Introdução às funções(def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parámetros(argumentos)
e retornar um valor específico.
Por padrao, funções ppython retornam none(nada)
"""

def example(parametro):
    return parametro
example('argumento')

def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
 
 
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)