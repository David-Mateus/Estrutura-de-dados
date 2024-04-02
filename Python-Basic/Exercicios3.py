tentativa_do_usuario = 0
palavra_usuario = ""
palavra_secreta = 'david'
while True:
    letra_digitada = input("Digite uma letra: ")[0].lower()
    tentativa_do_usuario +=1
    if letra_digitada in palavra_secreta:
        palavra_usuario += letra_digitada

    palavra_formada = ""
    for letra_secreta in palavra_secreta:
        if letra_secreta in palavra_usuario:
            palavra_formada += letra_secreta
        else:
            palavra_formada +='*'
            
    if palavra_formada == palavra_secreta:
        print("Voce ganhou")
        print(f"Voce teve {tentativa_do_usuario} tentativas")
        tentativa_do_usuario = 0
        palavra_usuario = ""
    
    




    
