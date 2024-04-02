"""
Formatação basica de strings
s-strings
d- int
f-float
.<numero de digitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
"""
variavel = "ABC"
print(f"{variavel}")
print(f"{variavel: >10}")
print(f"{variavel: <10}")
print(f"{variavel: ^10}")
print(f'{100.0000:.1f}')