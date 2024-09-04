# Lista para registrar as vendas
vendas = []


# Calcula e exibe o faturamento total e a quantidade de cada item vendido
def calcular_faturamento():
    if not vendas:
        print("\n> Nenhuma venda foi efetuada.")
        return

    # Calcula o faturamento total somando o total de cada venda
    total_vendas = sum(venda["total"] for venda in vendas)
    print(f"\nFaturamento Total: R$ {total_vendas:.2f}")

    # Dicionário para acumular a quantidade e o valor total de cada item vendido
    itens_vendidos = {}
    valor_total_itens = {}

    # Itera sobre cada venda para agregar as informações dos itens vendidos
    for venda in vendas:
        for item, detalhes in venda["itens"].items():
            quantidade = detalhes["quantidade"]
            valor = detalhes["valor"]

            # Atualiza a quantidade e o valor total dos itens vendidos
            if item in itens_vendidos:
                itens_vendidos[item] += quantidade
                valor_total_itens[item] += valor
            else:
                itens_vendidos[item] = quantidade
                valor_total_itens[item] = valor

    # Exibe o resumo dos itens vendidos
    print("\n> Resumo dos itens vendidos:\n")
    for item, quantidade in itens_vendidos.items():
        valor_total = valor_total_itens[item]
        print(f"{item}: {quantidade} unidade(s) - Valor Total: R$ {valor_total:.2f}")


# Exibe detalhes específicos sobre os produtos vendidos, incluindo código de barras e informações adicionais
def exibir_detalhes_produtos_vendidos():
    if not vendas:
        print("\n> Nenhuma venda foi efetuada.")
        return

    detalhes_vendidos = {}  # Dicionário para acumular os detalhes dos produtos vendidos

    # Itera sobre todas as vendas para compilar detalhes dos produtos vendidos
    for venda in vendas:
        produtos = venda["produtos"]  # Acessa a chave correta para obter os detalhes dos produtos
        
        # Itera sobre cada produto vendido
        for produto in produtos:
            nome_produto = produto["nome"]
            codigo_barras = produto["codigo_barra"]
            preco = produto["preco"]

            if nome_produto not in detalhes_vendidos:
                detalhes_vendidos[nome_produto] = {
                    "quantidade_total": 0,
                    "unidades": [],  # Lista para armazenar detalhes de cada unidade vendida
                    "produtos_por_recibo": {}  # Dicionário para armazenar os produtos separados por recibo
                }

            # Atualiza a quantidade total e detalhes de cada unidade vendida
            detalhes_vendidos[nome_produto]["quantidade_total"] += 1
            detalhes_vendidos[nome_produto]["unidades"].append({
                "codigo_barras": codigo_barras,
                "nome": nome_produto,
                "preco": preco
            })

            # Adiciona o produto ao dicionário de produtos por recibo
            recibo_id = venda.get("id", "Desconhecido")  # Obtém um identificador do recibo, se disponível
            if recibo_id not in detalhes_vendidos[nome_produto]["produtos_por_recibo"]:
                detalhes_vendidos[nome_produto]["produtos_por_recibo"][recibo_id] = {
                    "quantidade_total": 0,
                    "unidades": []  # Lista para armazenar detalhes de cada unidade vendida
                }
            
            detalhes_vendidos[nome_produto]["produtos_por_recibo"][recibo_id]["quantidade_total"] += 1
            
            detalhes_vendidos[nome_produto]["produtos_por_recibo"][recibo_id]["unidades"].append({
                "codigo_barras": codigo_barras,
                "nome": nome_produto,
                "preco": preco
            })

    # Exibe os detalhes dos produtos vendidos
    print("\n> Detalhes dos produtos vendidos:")
    for nome_produto, info in detalhes_vendidos.items():
        print(f"\nProduto: {nome_produto} - Total Vendido: {info['quantidade_total']} unidade(s)")

        for unidade in info["unidades"]:
            print(f"Código de Barras: {unidade['codigo_barras']}, Nome: {unidade['nome']}, Valor: R$ {unidade['preco']:.2f}")

        # Exibe os produtos separados por recibo
        for recibo_id, produtos_recibo in info["produtos_por_recibo"].items():
            print(f"\nRecibo ID: {recibo_id} - Produto: {nome_produto} - Total Vendido: {produtos_recibo['quantidade_total']} unidade(s)")
            
            for unidade in produtos_recibo["unidades"]:
                print(f"Código de Barras: {unidade['codigo_barras']}, Nome: {unidade['nome']}, Valor: R$ {unidade['preco']:.2f}")


# Exibe todos os recibos das vendas realizadas
def exibir_recibos():
    if not vendas:
        print("\n> Nenhuma venda foi efetuada.")
        return

    print("\n> Recibos das vendas efetuadas:")
    
    # Exibe a quantidade total de recibos expedidos
    total_recibos = len(vendas)
    print(f"\nTotal de recibos emitidos: {total_recibos}")

    # Itera sobre todas as vendas registradas
    for indice, venda in enumerate(vendas, start=1):
        print(f"\nRecibo #{indice}:")
        total_venda = venda["total"]
        itens = venda["itens"]

        # Itera sobre cada item da venda
        for nome_produto, detalhes in itens.items():
            quantidade = detalhes["quantidade"]
            valor_total_item = detalhes["valor"]
            valor_unitario = valor_total_item / quantidade  # Calcula o valor unitário

            print(f"- {nome_produto}: {quantidade} unidade(s) x R$ {valor_unitario:.2f} = Total: R$ {valor_total_item:.2f}")

        print(f"- Valor Total: R$ {total_venda:.2f}")

