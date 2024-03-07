nome = input("Nome do usuario: ")
idade = int(input("Idade: "))
if(nome and idade):
    print(f"Seu nome: {nome}")
    print(f"Nome invertido: {nome[::-1]}")
    print(f"Possui espacos: {' ' in nome}")
    print(f"Possui quantas lentras: {len(nome)}")
    print(f"Primeira letra: {nome[0]}")
    print(f"Ultima letra: {nome[-1]}")
else:
    print("Descula, voce deixou campos vazios")