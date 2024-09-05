from . import injecao_dados



# Exibe o título da seção de Teste
def exibir_titulo():
    print("\n\n\n=== Teste ==")


# Exibe o menu principal de Injeção de Dados
def exibir_menu():
    print("\n1. Injetar recibos de vendas")
    print("2. Injetar produtos indisponíveis")
    print("3. Adicionar produtos")
    print("0. Sair")

    return input("\n</> Escolha uma opção: ")


# Exibe a interface principal de Injeção de Dados
def exibir_interface():
    exibir_titulo()  # Exibe o título da seção

    while True:
        escolha = exibir_menu()  # Exibe o menu principal e obtém a escolha do usuário
        
        if escolha == "1":
            injecao_dados.injetar_recibos_vendas()  # Injeta os recibos de vendas
            continue

        elif escolha == "2":
            injecao_dados.injetar_produtos_indisponiveis()  # Injeta produtos indisponíveis
            continue

        elif escolha == "3":
            injecao_dados.atualizar_e_varrer_produtos()  # Atualiza e varre produtos
            continue

        elif escolha == "0":
            print("\n> Retornando...")  # Mensagem ao retornar do menu
            break

        else:
            print("\n! Opção inválida. Tente novamente.")  # Mensagem de erro para opções inválidas
            continue
