from datetime import datetime
try:
    numero = (input("Digite um valor inteiro: "))
    numero_int = int(numero)
    modulo_numero = numero_int % 2 == 0

    if modulo_numero:
        print(f"{numero_int} numero par")
    else:
        print(f"{numero_int} numero impar")

except:
    print(f"Error! Você digitou um {type(numero)}, mas o esperado é um inteiro")

try:
    hora_atual = datetime.now().time()
    hora_formatada = hora_atual.strftime("%H:%M:%S")
    hora_manha = str(hora_formatada) < '12:00:00'
    hora_tarde = str(hora_formatada) > '12:00:00' and hora_formatada < '18:00:00'
    

    if(hora_manha):
        print("Bom dia")
    elif(hora_tarde):
        print("Boa tarde")
    else:
        print("Boa Noite")
except:
    print("Hora não informada")

try:
    nome = input("Digite seu nome: ")
    tamanho_do_nome = len(nome)
    nome_curto = tamanho_do_nome <= 4
    nome_medio = tamanho_do_nome >= 5 and tamanho_do_nome <= 6

    if nome_curto:
        print("Seu nome é curto")
    elif nome_medio:
        print("Seu nome é normal")
    else:
        print("Seu nome é muito grande")
except:
    print("Você não digitou seu nome ou uma string")