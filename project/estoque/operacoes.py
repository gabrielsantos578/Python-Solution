from setor.administrativo import administrativo
from . import produtos



# Exibe todos os itens disponíveis em estoque, incluindo categoria, nome, código, quantidade, preço e códigos de barras vinculados.
def exibir_itens_disponiveis():
    disponiveis = False  # Flag para verificar se há itens disponíveis

    print("\n> Itens disponíveis:")
    for tipo, lista_produtos in produtos.tipos_produtos.items():
        # Filtra produtos que têm quantidade maior que zero
        produtos_disponiveis = [produto for produto in lista_produtos if produto["quantidade"] > 0]
        if produtos_disponiveis:
            print(f"\n\n{tipo.capitalize()}:")
            for produto in produtos_disponiveis:
                print(f"\nCódigo: {produto['codigo']}, Quantidade disponível: {produto['quantidade']}")
                
                # Exibe detalhes dos códigos de barras em linhas separadas
                for codigo_barras in produto["codigos_barras"]:
                    print(f"  Código de Barras: {codigo_barras}, Nome: {produto['nome']}, Valor: R$ {produto['preco']:.2f}")

                disponiveis = True  # Confirma que há itens disponíveis
    print()
    
    if not disponiveis:
        print("\n> Não há nenhum produto disponível.")


# Exibe todos os itens com quantidade zerada, incluindo categoria, nome, código, quantidade, preço e códigos de barras vinculados.
def exibir_itens_indisponiveis():
    # Verifica se há vendas registradas
    if not administrativo.vendas:
        print("\n> Não há produtos em falta.")
        return

    indisponiveis = set()
    for venda in administrativo.vendas:
        for item in venda["itens"]:
            indisponiveis.add(item)  # Armazena os nomes dos produtos vendidos

    print("\n> Itens indisponíveis:")
    for tipo, lista_produtos in produtos.tipos_produtos.items():
        # Filtra produtos com quantidade igual a zero e que foram vendidos
        produtos_indisponiveis = [produto for produto in lista_produtos if produto["nome"] in indisponiveis and produto["quantidade"] == 0]
        if produtos_indisponiveis:
            print(f"\n{tipo.capitalize()}:")
            for produto in produtos_indisponiveis:
                print(f"Código: {produto['codigo']}, Nome: {produto['nome']}, Quantidade: {produto['quantidade']}, Preço: R$ {produto['preco']:.2f}")
