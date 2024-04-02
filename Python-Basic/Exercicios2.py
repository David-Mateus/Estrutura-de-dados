"""
Iterando strings com while
"""
# nome = "David Mateus"

# x = 0
# tamanho_do_nome = len(nome)
# while x < tamanho_do_nome:
#     print("*"+nome[x], end="")
#     x+=1
"""Calculadora com While"""

while True:
    print("""
- Somar(1)
- Subtrair(2)
- Dividir(3)
- Multiplicar(4)
- Sair(0)
""")
    try:
        escolha_usuario = int(input("Escolhar a operação: "))

        if escolha_usuario == 0:
            print("Programa finalizado")
            break

        numero_1 = int(input("Digite um numero: "))
        numero_2 = int(input("Digite outro numero: "))

        if escolha_usuario == 1:
            print(f"Resultado: {numero_1+numero_2}")
        elif escolha_usuario == 2:
            print(f"Resultado: {numero_1-numero_2}")
        elif escolha_usuario == 3:
            print(f"Resultado: {numero_1//numero_2}")
        elif escolha_usuario == 4:
            print(f"Resultado: {numero_1*numero_2}")
        else:
            print("Opção inválida")
    
    except Exception:
        print("Você digitou um valor fora da escolhar")
    
