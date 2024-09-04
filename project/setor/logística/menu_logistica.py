from estoque import operacoes



# Exibe o título da seção de logística
def exibir_titulo():
    print("\n\n\n=== Logística ===")


# Exibe o menu de opções para a seção de logística
def exibir_menu():
    print("\n1. Exibir produtos disponíveis")
    print("2. Exibir produtos indisponíveis")
    print("0. Sair")
    
    return input("\n</> Escolha uma opção: ")


# Exibe a interface de logística e gerencia as escolhas do logístico
def exibir_interface():
    exibir_titulo()  # Mostra o título da seção

    while True:
        escolha = exibir_menu()  # Exibe o menu e obtém a escolha do logístico
        
        if escolha == "1":
            operacoes.exibir_itens_disponiveis()  # Exibe detalhes dos produtos disponíveis
            continue

        elif escolha == "2":
            operacoes.exibir_itens_indisponiveis()  # Exibe detalhes dos produtos indisponíveis
            continue

        elif escolha == "0":
            print("\n> Retornando...")  # Mensagem de retorno
            break

        else:
            print("\n! Opção inválida. Tente novamente.")  # Mensagem de erro para opção inválida
            continue
