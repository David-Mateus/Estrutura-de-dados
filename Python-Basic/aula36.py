"""
Iteravel -L str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entegue seu iterador
"""
#O que o for faz por baixo dos panos
texto = 'David'
iterador = iter(texto)
while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break

for letra in texto:
    print(letra)