from . import caixa



# Exibe o título da seção de Caixa
def exibir_titulo():
    print("\n\n\n=== Caixa ==\n")


# Exibe o título da seção de Nova Venda
def exibir_titulo_venda():
    print("\n\n\n=== Nova Venda ==\n")


# Exibe o menu principal de Caixa
def exibir_menu():
    print("1. Nova venda")
    print("0. Sair")
    
    return input("\n</> Escolha uma opção: ")


# Exibe o menu de vendas se houver itens no carrinho
def exibir_menu_venda():
    print("\n1. Adicionar items")
    if caixa.venda:
        print("2. Remover items")
        print("3. Finalizar venda")
    print(f"0. {'Cancelar venda' if caixa.venda else 'Sair'}")
    
    return input("\n</> Escolha uma opção: ")


# Exibe a interface principal de Caixa
def exibir_interface():
    exibir_titulo()  # Exibe o título da seção

    while True:
        escolha = exibir_menu()  # Exibe o menu principal e obtém a escolha do funcionário
        
        if escolha == "1":
            exibir_interface_venda()  # Exibe a interface de venda
            exibir_titulo()  # Exibe o título novamente após retornar da interface de venda
            continue

        elif escolha == "0":
            print("\n> Retornando...")  # Mensagem ao retornar do menu
            break

        else:
            print("\n! Opção inválida. Tente novamente.")  # Mensagem de erro para opções inválidas
            continue


# Exibe a interface de nova venda
def exibir_interface_venda():
    while True:
        escolha = exibir_menu_venda()  # Exibe o menu de venda e obtém a escolha do funcionário
        
        if escolha == "1":
            caixa.nova_venda()  # Adiciona novos itens ao carrinho
            continue

        elif escolha == "2" and caixa.venda:
            caixa.remover_produto()  # Remove itens do carrinho
            continue

        elif escolha == "3" and caixa.venda:
            caixa.encerrar_compra()  # Finaliza a venda
            break

        elif escolha == "0":
            if caixa.venda:
                print("\n> Cancelando...")
                caixa.venda.clear()  # Cancela a venda e limpa o carrinho
                print("> Venda cancelada.")

            print("\n> Retornando...")  # Mensagem ao retornar do menu
            break

        else:
            print("\n! Opção inválida. Tente novamente.")  # Mensagem de erro para opções inválidas
            continue
