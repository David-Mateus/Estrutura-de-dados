"""
Argumentos nomeados e não nomeados em funções python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento(valor)"""
#Paamentro usa-se na definição da função e argumentos usa-se no valor da função

#Argumentos não nomeados
def soma(x, y):
    print(x, y)
soma(1,2)
#Argumentos noemados
soma(y=2, x=1)