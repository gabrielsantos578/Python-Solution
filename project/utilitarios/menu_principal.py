from setor import menu_administrativo
from usuario import menu_cliente 



def exibir_titulo():
    print("\n=== Supermercado ===")


def exibir_menu():
    print("1. Administrativo")
    print("2. Cliente")
    print("0. Encerrar")
    
    return input("Escolha uma opção: ")


def exibir_interface():
    exibir_titulo()

    while True:
        escolha = exibir_menu()
        
        if escolha == "1":
            menu_administrativo.exibir_interface()
            exibir_titulo()
            continue

        elif escolha == "2":
            menu_cliente.exibir_interface()
            exibir_titulo()
            continue

        elif escolha == "0":
            break

        else:
            print("Opção inválida. Tente novamente.")
            continue