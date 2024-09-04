from setor.administrativo import menu_administrativo
from setor.logística import menu_logistica
from caixa import menu_caixa



# Função para exibir o título principal da aplicação
def exibir_titulo():
    print("\n\n\n=== Supermercado ===\n")


# Função para exibir o menu principal e retornar a escolha do usuário
def exibir_menu():
    print("1. Administrativo")
    print("2. Logística")
    print("3. Caixa")
    print("0. Encerrar")
    
    return input("\n</> Escolha uma opção: ")


# Função para gerenciar a interface principal da aplicação
def exibir_interface():
    exibir_titulo()  # Exibe o título inicial

    while True:
        escolha = exibir_menu()  # Exibe o menu e armazena a escolha do usuário
        
        # Opção para acessar o menu administrativo
        if escolha == "1":
            menu_administrativo.exibir_interface()
            exibir_titulo()  # Exibe o título novamente após retornar do menu administrativo
            continue

        # Opção para acessar o menu de logística
        elif escolha == "2":
            menu_logistica.exibir_interface()
            exibir_titulo()  # Exibe o título novamente após retornar do menu de logística
            continue

        # Opção para acessar o menu do caixa
        elif escolha == "3":
            menu_caixa.exibir_interface()
            exibir_titulo()  # Exibe o título novamente após retornar do menu do caixa
            continue

        # Opção para encerrar a aplicação
        elif escolha == "0":
            print("\n> Aplicação Encerrada\n\n\n")
            break

        # Tratamento para opções inválidas
        else:
            print("\n! Opção inválida. Tente novamente.")
            continue
    