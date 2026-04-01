def gerenciar_lista_compras():
    lista = []
    
    while True:
        print("\n--- Lista de Compras ---")
        print("1. Adicionar item")
        print("2. Visualizar lista")
        print("3. Remover item")
        print("4. Sair")
        
        opcao = input("\nEscolha uma opção (1-4): ")
        
        if opcao == '1':
            item = input("Digite o nome do item a ser adicionado: ")
            lista.append(item)
            print(f"-> '{item}' foi adicionado com sucesso!")
            
        elif opcao == '2':
            if not lista:
                print("-> A lista está vazia no momento.")
            else:
                print("\nItens na sua lista:")
                for i, item in enumerate(lista, start=1):
                    print(f"{i}. {item}")
                    
        elif opcao == '3':
            if not lista:
                print("-> A lista já está vazia.")
            else:
                print("\nItens atuais:")
                for i, item in enumerate(lista, start=1):
                    print(f"{i}. {item}")
                
                try:
                    indice = int(input("Digite o número do item que deseja remover: ")) - 1
                    if 0 <= indice < len(lista):
                        item_removido = lista.pop(indice)
                        print(f"-> '{item_removido}' foi removido da lista!")
                    else:
                        print("-> Erro: Número de item inválido.")
                except ValueError:
                    print("-> Erro: Por favor, digite apenas o número correspondente ao item.")
                    
        elif opcao == '4':
            print("-> Saindo do aplicativo de lista de compras. Até logo!")
            break
            
        else:
            print("-> Opção inválida. Por favor, escolha um número entre 1 e 4.")

if __name__ == "__main__":
    gerenciar_lista_compras()
