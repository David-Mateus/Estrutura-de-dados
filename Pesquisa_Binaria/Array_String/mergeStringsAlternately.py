str1 = 'abc'
str2 = 'pqr'
resultado = ''
tamanho = min(len(str1), len(str2))
for i in range(tamanho):
    resultado += str1[i] + str2[i]
print(resultado)

    