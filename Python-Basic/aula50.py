# Gerando cpf
import random
for _ in range(20):

    cpf = ''
    for i in range(9):
        cpf += str(random.randint(0,9))

    contador_regressivo_1 = 10
    noves_digitos = cpf[0:9]

    sum_value_cpf = 0
    for digito in noves_digitos:
        sum_value_cpf += int(digito) * contador_regressivo_1
        contador_regressivo_1 -=1
        

    resto_da_divisao_1 = ((sum_value_cpf * 10) % 11)
    resto_da_divisao_1 = resto_da_divisao_1 if resto_da_divisao_1 <= 9 else 0


    contador_regressivo = 11
    dez_digitos = cpf[0:10]

    sum_value_cpf_2 = 0
    for digito in dez_digitos:
        sum_value_cpf_2 += int(digito) * contador_regressivo
        contador_regressivo -=1
        

    resto_da_divisao_2 = ((sum_value_cpf_2 * 10) % 11)
    resto_da_divisao_2 = resto_da_divisao_2 if resto_da_divisao_2 <= 9 else 0

    print(f"{noves_digitos}{resto_da_divisao_1}{resto_da_divisao_2}")
