from estoque import produtos, operacoes
from setor import administrativo



# Lista de compras e registro de vendas
compras_usuario = []


def selecionar_item_para_compra():
    while True:
        operacoes.exibir_itens_disponiveis()
        nome_produto = input("\nDigite o nome do produto que deseja comprar (ou 'encerrar' para finalizar): ")
        
        if nome_produto.lower() == "encerrar":
            encerrar_compra(compras_usuario)
            break

        quantidade = int(input("Digite a quantidade desejada: "))
        adicionar_produtos_a_compra(nome_produto, quantidade)


def adicionar_produtos_a_compra(nome_produto, quantidade):
    produtos_adicionados = 0
    
    for tipo, lista_produtos in produtos.tipos_produtos.items():
        produtos_a_remover = []
        for produto in lista_produtos:
            if produto["nome"].lower() == nome_produto.lower() and produtos_adicionados < quantidade:
                compras_usuario.append(produto)
                produtos_a_remover.append(produto)
                produtos_adicionados += 1

        # Remove produtos já adicionados da lista original
        for produto_removido in produtos_a_remover:
            lista_produtos.remove(produto_removido)

        if produtos_adicionados == quantidade:
            break

    if produtos_adicionados == quantidade:
        total = sum([p["preco"] for p in compras_usuario if p["nome"].lower() == nome_produto.lower()])
        print(f"\nVocê adicionou {quantidade}x {nome_produto} - Total parcial: R$ {total:.2f}")
    else:
        print(f"\nNão há estoque suficiente de {nome_produto}. Apenas {produtos_adicionados} adicionado(s).")


def encerrar_compra(itens_selecionados):
    """Finaliza a compra e gera o recibo."""
    total = 0.0
    recibo = {}
    
    # Processa cada item selecionado
    for produto in itens_selecionados:
        # Atualiza o total e recibo
        total += produto["preco"]
        if produto["nome"] in recibo:
            recibo[produto["nome"]] += 1
        else:
            recibo[produto["nome"]] = 1

    # Registra a venda
    administrativo.vendas.append({"itens": recibo, "total": total})
    
    # Exibe o recibo
    print("\nItens comprados:")
    for nome, quantidade in recibo.items():
        print(f"{nome} x{quantidade}")
    
    print(f"Total: R$ {total:.2f}\n")
    compras_usuario.clear()
