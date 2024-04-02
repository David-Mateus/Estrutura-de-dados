"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
# While simples
# x = 10
# i = 0
# while i < x:
#     print(i)
#     i += 1

# condicao = True
# while condicao:
#     x = int(input("Digite um valor != 0(parar)"))
#     if x == 0:
#         condicao = False
#         print("Parou")
#     else:
#         print("Rodando")

# contador = 0
# while contador <= 10:
#     contador+=1
#     print(contador)
    
#Operadores de atribuição
# = += -= *= /= //= **= %=

#Laços internos
    
qtd_linhas = 5
qtd_colunas = 5
linha = 1
while linha <= qtd_linhas: #1x
    coluna = 1
    while coluna <= qtd_colunas: #5x
        
        print(f"linha: {linha} coluna {coluna}")
        coluna +=1
    linha +=1
    
    
print("Acabou")