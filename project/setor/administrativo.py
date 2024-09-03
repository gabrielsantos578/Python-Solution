vendas = []


def calcular_faturamento():
    """Calcula e exibe o faturamento total."""
    total_vendas = sum(venda["total"] for venda in vendas)
    print(f"\nFaturamento Total: R$ {total_vendas:.2f}")
    print("Itens vendidos:")
    for venda in vendas:
        for item, quantidade in venda["itens"].items():
            print(f"{item}: {quantidade} unidade(s)")