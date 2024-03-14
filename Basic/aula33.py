# frase = "aaaaabbbbbbbbbbb"

# tamanho_da_frase = len(frase)
# x = 0
# qtd_apareceu_mais_vezes = 0
# letra_apareceu_mais_vezes = ''
# while x < tamanho_da_frase:
#     letra_atual = frase[x]
#     qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)
#     if letra_atual == ' ':
#         x+=1
#         continue
#     if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
#         qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
#         letra_que_mais_apraceu = letra_atual
    
#     x+=1
# print(letra_atual, qtd_apareceu_mais_vezes)

    



linhas = 2
colunas = 2
 
linha = 1
while linha <= linhas:
    coluna = 1
    while coluna <= colunas:
        print(linha, coluna)
        coluna += 1
    linha += 1