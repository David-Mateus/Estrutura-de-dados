# Abre um arquivo chamado "exemplo.txt" para leitura
with open('exemplo.txt', 'r') as arquivo:
    # Faça algo com o conteúdo do arquivo
    conteudo = arquivo.read()
    print(conteudo)
