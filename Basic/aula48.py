cpf = '74682489070'
count = 10
pegando_nove = cpf[0:9]
value = []
sum_value_cpf = 0
for i in pegando_nove:
    x = int(i) * count
    count -=1
    value.append(x)
    sum_value_cpf += x

x = sum_value_cpf * 10
print(x%11)