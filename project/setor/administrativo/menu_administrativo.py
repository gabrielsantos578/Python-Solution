from . import administrativo



# Exibe o título da seção administrativa
def exibir_titulo():
    print("\n\n\n=== Administrativo ===")


# Exibe o menu de opções para a seção administrativa
def exibir_menu():
    print("\n1. Exibir faturamento")
    print("2. Exibir recibos")
    print("3. Exibir produtos vendidos")
    print("0. Sair")
    
    return input("\n</> Escolha uma opção: ")


# Gerencia a interface do menu administrativo e executa a ação correspondente à escolha do administrador
def exibir_interface():
    exibir_titulo()  # Exibe o título da seção administrativa

    while True:
        escolha = exibir_menu()  # Exibe o menu e obtém a escolha do administrador
        
        if escolha == "1":
            # Exibe o faturamento total e a quantidade de cada item vendido
            administrativo.calcular_faturamento()
            continue

        elif escolha == "2":
            # Exibe todos os recibos das vendas realizadas
            administrativo.exibir_recibos()
            continue

        elif escolha == "3":
            # Exibe detalhes específicos sobre os produtos vendidos, incluindo código de barras e informações adicionais
            administrativo.exibir_detalhes_produtos_vendidos()
            continue

        elif escolha == "0":
            print("\n> Retornando...")  # Mensagem de retorno ao menu anterior
            break

        else:
            print("\n! Opção inválida. Tente novamente.")  # Mensagem de erro para opção inválida
            continue
