list_item = []
price_item = []
total = 0
while True:
    print("=== Bem-vindo a sua lista de compras ===")
    print("=== Instruções de uso: Produto: Loren Ipsun")
    print("""
        1.Adicionar
        2.Atualizar
        3.Remover
        4.Listar
        5.Total
        6.Sair
        """)
    try:
        option_choice = int(input("Escolha: "))
        
        
        if option_choice == 1:
            name_product = input("Nome do produto: ").lower()
            price_product = float(input("Preço do produto: "))
            list_item.append(name_product)
            price_item.append(price_product)
            
        elif option_choice == 2:
            name_product_old = input("Digite o nome do produto: ").lower()
            name_update = input("Digite o novo nome: ").lower()
            for i in range(len(list_item)):
                if list_item[i] == name_product_old:
                    list_item = name_update
                else:
                    print("Nome não está cadastro na lista")
        elif option_choice == 3:
            name_product_delete = input("Digite o nome do produto a ser apagado: ")
            if name_product_delete:
                list_item.remove(name_product_delete)
                print(f"Item removido: {name_product_delete}")
            else:
                print("Item não encontrado!")
        elif option_choice == 4:
            for index, name in enumerate(list_item):
                print(index, name, end="")
        elif option_choice == 5:
            for i in range(len(list_item)):
                total += price_item[i]
            print(f"Total {total}")
        else:
            break
                    

    except:
        print("Error")

