from . import produtos



def exibir_itens_disponiveis():
    """Exibe todos os itens disponíveis em estoque."""
    print("\nItens disponíveis:")
    for tipo, lista_produtos in produtos.tipos_produtos.items():
        print(f"\n{tipo.capitalize()}:")
        produtos_contados = {}
        for produto in lista_produtos:
            if produto["nome"] in produtos_contados:
                produtos_contados[produto["nome"]] += 1
            else:
                produtos_contados[produto["nome"]] = 1
        
        for nome, quantidade in produtos_contados.items():
            print(f"{nome}: {quantidade} disponíveis")


def exibir_itens_indisponiveis():
    """Exibe todos os itens que não estão mais disponíveis em estoque."""
    print("\nItens indisponíveis:")
    for tipo, lista_produtos in produtos.tipos_produtos.items():
        indisponiveis = set()
        for produto in lista_produtos:
            indisponiveis.add(produto["nome"])
        for item in indisponiveis:
            if len([p for p in lista_produtos if p["nome"] == item]) == 0:
                print(item)
