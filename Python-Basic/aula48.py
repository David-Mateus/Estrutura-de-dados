#Calculo do primeiro digito do CPF
cpf = '37696055003'
contador_regressivo = 10
noves_digitos = cpf[0:9]

sum_value_cpf = 0
for digito in noves_digitos:
    sum_value_cpf += int(digito) * contador_regressivo
    contador_regressivo -=1
    

resto_da_divisao = ((sum_value_cpf * 10) % 11)
resto_da_divisao = resto_da_divisao if resto_da_divisao <= 9 else 0
print(resto_da_divisao)
