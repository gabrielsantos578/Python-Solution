from . import cliente



def exibir_titulo():
    print("\n=== Cliente ===")


def exibir_menu():
    print("1. Selecionar itens para compra")
    print("2. Encerrar compra")
    print("0. Sair")
    
    return input("Escolha uma opção: ")


def exibir_interface():
    exibir_titulo()

    while True:
        escolha = exibir_menu()
        
        if escolha == "1":
            cliente.selecionar_item_para_compra()
            continue

        elif escolha == "2":
            cliente.encerrar_compra()
            continue

        elif escolha == "0":
            break

        else:
            print("Opção inválida. Tente novamente.")
            continue