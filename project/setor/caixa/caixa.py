from setor.estoque import produtos
from setor.administrativo import administrativo



# Lista para armazenar os produtos da venda atual
venda = []


# Inicia o processo de uma nova venda
def nova_venda():
    while True:
        if not adicionar_produto():  # Adiciona produtos até o funcionário desejar parar
            if venda:
                mostrar_produtos_selecionados()  # Mostra o resumo dos produtos selecionados
            break  # Sai do loop se o funcionário deseja terminar a adição de produtos


# Adiciona um produto ao carrinho usando o código de barras
def adicionar_produto():
    codigo_barra = input("\n</> Informe o código de barras do produto (ou '0' para terminar): ")

    if codigo_barra == "0":
        return False  # Indica que o funcionário deseja terminar a adição de produtos

    produto_encontrado = None
    # Procura o produto no estoque usando o código de barras
    for tipo, lista_produtos in produtos.tipos_produtos.items():
        for produto in lista_produtos:
            if codigo_barra in produto["codigos_barras"]:
                produto_encontrado = produto
                break
        if produto_encontrado:
            break

    if produto_encontrado:
        # Verifica se o produto já está no carrinho
        produto_no_carrinho = next((item for item in venda if item["codigo_barra"] == codigo_barra), None)
        if produto_no_carrinho:
            print(f"! Este código de barras {codigo_barra} já foi adicionado ao carrinho.")
        else:
            venda.append({"codigo_barra": codigo_barra, "produto": produto_encontrado})
            print(f"\n> Item adicionado: Código de Barras: {codigo_barra}, Nome: {produto_encontrado['nome']}, R$ {produto_encontrado['preco']:.2f}")
    else:
        print("\n! Código de barras não encontrado. Tente novamente.")

    return True  # Indica que a adição foi concluída e o funcionário pode continuar


# Interface para confirmar se o funcionário deseja remover
def remover_produto():
    while True:
        remover = input("\n</> Deseja remover algum produto do carrinho? (s/n): ").lower()
        if remover == "s":
            produtos_selecionados_para_remover()  # Exibe os produtos para remoção
            remover_produto_por_barra()  # Remove um produto pelo código de barras

            if not venda:  # Se o carrinho estiver vazio, sai do loop
                break

        elif remover == "n":
            break
        else:
            print("\n! Opção inválida. Tente novamente.")


# Exibe a série e o nome dos produtos atualmente no carrinho para remoção
def produtos_selecionados_para_remover():
    print("\nProdutos para remoção:")
    for item in venda:
        print(f"Código de Barras: {item['codigo_barra']}, Nome: {item['produto']['nome']}")


# Permite remover um item do carrinho usando o código de barras
def remover_produto_por_barra(): 
    codigo_barra = input("\n</> Informe o código de barras do produto (ou '0' para terminar): ")

    if codigo_barra == "0":
        return False  # Indica que o funcionário deseja terminar a remoção de produtos

    produto_removido = False
    # Procura o produto no carrinho e remove se encontrado
    for item in venda:
        if item["codigo_barra"] == codigo_barra:
            venda.remove(item)
            produto_removido = True
            print(f"\n> Produto removido: Código de Barras {codigo_barra}, {item['produto']['nome']}")
            break

    if not produto_removido:
        print("\n! Código de barras não encontrado no carrinho.")


# Exibe os produtos atualmente no carrinho, incluindo quantidade total e valor
def mostrar_produtos_selecionados():
    recibo = {}
    for item in venda:
        produto = item["produto"]
        if produto["nome"] in recibo:
            recibo[produto["nome"]]["quantidade"] += 1
            recibo[produto["nome"]]["valor"] += produto["preco"]
        else:
            recibo[produto["nome"]] = {"quantidade": 1, "valor": produto["preco"]}

    print("\n> Produtos selecionados:")
    for nome, detalhes in recibo.items():
        print(f"{detalhes['quantidade']}x {nome} - R$ {detalhes['valor']:.2f}")


# Interface para confirmar se o funcionário deseja encerrar
def encerrar_compra():
    while True:
        encerrar = input("\n</> Deseja encerrar a venda? (s/n): ").lower()
        if encerrar == "s":
            encerrar_compra_e_salvar()  # Finaliza a compra e salva o recibo
            break
        elif encerrar == "n":
            break
        else:
            print("! Opção inválida. Tente novamente.")


# Finaliza a compra, gera o recibo, salva a venda e ajusta o estoque
def encerrar_compra_e_salvar():
    total = 0.0
    recibo = {}
    produtos_vendidos = []

    for item in venda:
        produto = item["produto"]
        codigo_barra = item["codigo_barra"]
        total += produto["preco"]
        if produto["nome"] in recibo:
            recibo[produto["nome"]]["quantidade"] += 1
            recibo[produto["nome"]]["valor"] += produto["preco"]
        else:
            recibo[produto["nome"]] = {"quantidade": 1, "valor": produto["preco"]}

        produtos_vendidos.append(
            {"codigo_barra": codigo_barra, "nome": produto["nome"], "preco": produto["preco"]}
        )

    # Exibe o recibo
    print("\n> Itens comprados:")
    for nome, detalhes in recibo.items():
        print(f"{detalhes['quantidade']}x {nome} - R$ {detalhes['valor']:.2f}")

    print(f"Total: R$ {total:.2f}")

    # Ajusta o estoque e remove códigos de barras
    for item in venda:
        produto = item["produto"]
        codigo_barra = item["codigo_barra"]

        # Remove o código de barras do estoque
        if codigo_barra in produto["codigos_barras"]:
            produto["codigos_barras"].remove(codigo_barra)
            produto["quantidade"] -= 1

    # Registra a venda
    administrativo.vendas.append(
        {"itens": recibo, "total": total, "produtos": produtos_vendidos}
    )

    # Limpa o carrinho do funcionário
    venda.clear()
