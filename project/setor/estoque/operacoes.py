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


# Função para varrer a lista de produtos e identificar os indisponíveis
def varrer_produtos_indisponiveis():
    indisponiveis = []  # Lista para armazenar produtos indisponíveis

    # Itera sobre todas as categorias de produtos
    for tipo, lista_produtos in produtos.tipos_produtos.items():
        # Verifica cada produto e adiciona à lista se a quantidade for zero
        for produto in lista_produtos:
            if produto["quantidade"] == 0:
                produto_indisponivel = {
                    "tipo": tipo,
                    "codigo": produto["codigo"],
                    "nome": produto["nome"],
                    "preco": produto["preco"],
                    "codigos_barras": produto["codigos_barras"]
                }
                indisponiveis.append(produto_indisponivel)
                
                # Adiciona o produto à lista de produtos indisponíveis, se não estiver lá
                if produto_indisponivel not in produtos.produtos_indisponiveis:
                    produtos.produtos_indisponiveis.append(produto_indisponivel)

    return indisponiveis


# Função para exibir os produtos indisponíveis, chamando a varredura
def exibir_itens_indisponiveis():
    produtos_indisponiveis = varrer_produtos_indisponiveis()

    if not produtos_indisponiveis:
        print("\n> Não há produtos indisponíveis no momento.")
        return

    print("\n> Itens indisponíveis:")

    categorias = {}

    # Agrupa os produtos por categoria
    for produto in produtos_indisponiveis:
        tipo = produto['tipo'].capitalize()
        if tipo not in categorias:
            categorias[tipo] = []
        categorias[tipo].append(f"Código: {produto['codigo']}, Nome: {produto['nome']}")

    # Exibe os produtos agrupados por categoria
    for categoria, itens in categorias.items():
        print(f"\n{categoria}:")
        for item in itens:
            print(f"{item}")
