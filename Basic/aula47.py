"""
Operação ternaria(condicional de um linha)
valor if condiçao else outro valor
"""
#condicao = 10 == 11
# variavel = valor if condical else outro valor
digito = int(input("valor: " ))
novo_digito = digito  if digito <= 9 else 0

print(novo_digito)