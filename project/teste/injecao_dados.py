from setor.administrativo import administrativo
from setor.estoque import produtos, operacoes


# Função para injetar recibos na lista de vendas e atualizar o estoque
def injetar_recibos_vendas():
    recibos = [
        {
            "id": "Recibo #1",
            "itens": {
                "Água": {"quantidade": 1, "valor": 2.0}
            },
            "total": 2.0,
            "produtos": [
                {"codigo_barra": "1001110000", "nome": "Água", "preco": 2.0}
            ]
        },
        {
            "id": "Recibo #2",
            "itens": {
                "Refrigerante": {"quantidade": 1, "valor": 4.0},
                "Água": {"quantidade": 1, "valor": 2.0}
            },
            "total": 6.0,
            "produtos": [
                {"codigo_barra": "1001100000", "nome": "Refrigerante", "preco": 4.0},
                {"codigo_barra": "1001110001", "nome": "Água", "preco": 2.0}
            ]
        },
        {
            "id": "Recibo #3",
            "itens": {
                "Arroz": {"quantidade": 1, "valor": 5.0},
                "Feijão": {"quantidade": 1, "valor": 7.0},
                "Refrigerante": {"quantidade": 1, "valor": 4.0},
                "Água": {"quantidade": 1, "valor": 2.0}
            },
            "total": 18.0,
            "produtos": [
                {"codigo_barra": "1001001000", "nome": "Arroz", "preco": 5.0},
                {"codigo_barra": "1001011000", "nome": "Feijão", "preco": 7.0},
                {"codigo_barra": "1001100001", "nome": "Refrigerante", "preco": 4.0},
                {"codigo_barra": "1001110010", "nome": "Água", "preco": 2.0}
            ]
        },
        {
            "id": "Recibo #4",
            "itens": {
                "Sabonete": {"quantidade": 1, "valor": 1.5},
                "Shampoo": {"quantidade": 1, "valor": 8.0}
            },
            "total": 9.5,
            "produtos": [
                {"codigo_barra": "1010000000", "nome": "Sabonete", "preco": 1.5},
                {"codigo_barra": "1010010000", "nome": "Shampoo", "preco": 8.0}
            ]
        }
    ]

    administrativo.vendas.extend(recibos)
    print("\n> Recibos injetados na lista de vendas com sucesso.")

    for recibo in recibos:
        for produto in recibo['produtos']:
            codigo_barra = produto['codigo_barra']
            nome = produto['nome']
            preco = produto['preco']
            quantidade_vendida = next(
                (item['quantidade'] for item in recibo['itens'].values() if item['valor'] == preco), 0
            )

            produto_encontrado = False
            for tipo, lista_produtos in produtos.tipos_produtos.items():
                for item in lista_produtos:
                    if codigo_barra in item['codigos_barras']:
                        produto_encontrado = True
                        item['quantidade'] -= quantidade_vendida

                        if codigo_barra in item['codigos_barras']:
                            item['codigos_barras'].remove(codigo_barra)

                        if item['quantidade'] <= 0:
                            produtos.produtos_indisponiveis.append({
                                "tipo": tipo,
                                "codigo": item['codigo_barra'],
                                "nome": item['nome'],
                                "preco": item['preco'],
                                "codigos_barras": item['codigos_barras']
                            })
                            lista_produtos.remove(item)
                        break

            if not produto_encontrado:
                print(f"\n> Aviso: Produto com código de barras '{codigo_barra}' não encontrado no estoque.")


# Função para injetar produtos na lista de produtos indisponíveis
def injetar_produtos_indisponiveis():
    nova_categoria = "tecnologia"

    # Dados dos produtos indisponíveis a serem injetados
    produtos_indisponiveis = [
        {
            "tipo": nova_categoria,
            "codigo_barra": "2000010000",
            "codigo": "4001",
            "nome": "Mouse",
            "preco": 30.00,
            "quantidade": 0,
            "codigos_barras": ["2000010000"],
        },
        {
            "tipo": nova_categoria,
            "codigo_barra": "2000020000",
            "codigo": "4002",
            "nome": "Teclado",
            "preco": 50.00,
            "quantidade": 0,
            "codigos_barras": ["2000020000"],
        },
    ]

    # Adiciona a nova categoria ao dicionário de tipos de produtos, se não existir
    if nova_categoria not in produtos.tipos_produtos:
        produtos.tipos_produtos[nova_categoria] = []

    # Adiciona os produtos à nova categoria
    produtos.tipos_produtos[nova_categoria].extend(produtos_indisponiveis)
    print("\n> Produtos indisponíveis injetados na nova categoria 'tecnologia'.")


# Função para atualizar e varrer produtos, injetando novos produtos e realizando varredura de indisponíveis
def atualizar_e_varrer_produtos():
    nova_categoria = "tecnologia"

    # Dados dos produtos com valor a serem injetados
    produtos_com_valor = [
        {
            "tipo": nova_categoria,
            "codigo_barra": "2000010000",
            "codigo": "4001",
            "nome": "Mouse",
            "preco": 30.00,
            "quantidade": 0,
            "codigos_barras": ["2000010000"],
        },
        {
            "tipo": nova_categoria,
            "codigo_barra": "2000020000",
            "codigo": "4002",
            "nome": "Teclado",
            "preco": 50.00,
            "quantidade": 0,
            "codigos_barras": ["2000020000"],
        },
    ]

    # Adiciona a nova categoria ao dicionário de tipos de produtos, se não existir
    if nova_categoria not in produtos.tipos_produtos:
        produtos.tipos_produtos[nova_categoria] = []

    # Adiciona os produtos à nova categoria
    produtos.tipos_produtos[nova_categoria].extend(produtos_com_valor)

    # Chama a função de varredura para atualizar a lista de produtos indisponíveis
    operacoes.varrer_produtos_indisponiveis()

    print("\n> Produtos com valor injetados e varredura realizada com sucesso.")
