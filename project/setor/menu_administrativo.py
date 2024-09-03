from estoque import operacoes
from . import administrativo



def exibir_titulo():
    print("\n=== Administrativo ===")


def exibir_menu():
    print("1. Exibir itens disponíveis")
    print("2. Exibir itens indisponíveis")
    print("3. Exibir faturamento")
    print("0. Sair")
    
    return input("Escolha uma opção: ")


def exibir_interface():
    exibir_titulo()

    while True:
        escolha = exibir_menu()
        
        if escolha == "1":
            operacoes.exibir_itens_disponiveis()
            continue

        elif escolha == "2":
            operacoes.exibir_itens_indisponiveis()
            continue

        elif escolha == "3":
            administrativo.calcular_faturamento()
            continue

        elif escolha == "0":
            break

        else:
            print("Opção inválida. Tente novamente.")
            continue