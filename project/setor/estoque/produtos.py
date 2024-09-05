# Listas de produtos com detalhes como tipo, código de barras binário, código, nome, preço, quantidade e números de série
alimentos = [
    {"tipo": "alimento", "codigo_barra": "100100", "codigo": "1001", "nome": "Arroz", "preco": 5.0, "quantidade": 10, 
     "codigos_barras": ["1001001000", "1001001001", "1001001010", "1001001011", "1001001100", "1001001101", "1001001110", "1001001111", "1001010000", "1001010001"]},
     
    {"tipo": "alimento", "codigo_barra": "100101", "codigo": "1002", "nome": "Feijão", "preco": 7.0, "quantidade": 8, 
     "codigos_barras": ["1001011000", "1001011001", "1001011010", "1001011011", "1001011100", "1001011101", "1001011110", "1001011111"]}
]

bebidas = [
    {"tipo": "bebida", "codigo_barra": "100110", "codigo": "2001", "nome": "Refrigerante", "preco": 4.0, "quantidade": 5, 
     "codigos_barras": ["1001100000", "1001100001", "1001100010", "1001100011", "1001100100"]},

    {"tipo": "bebida", "codigo_barra": "100111", "codigo": "2002", "nome": "Água", "preco": 2.0, "quantidade": 12, 
     "codigos_barras": ["1001110000", "1001110001", "1001110010", "1001110011", "1001110100", "1001110101", "1001110110", "1001110111", "1001111000", "1001111001", "1001111010", "1001111011"]}
]

higiene = [
    {"tipo": "higiene", "codigo_barra": "101000", "codigo": "3001", "nome": "Sabonete", "preco": 1.5, "quantidade": 7, 
     "codigos_barras": ["1010000000", "1010000001", "1010000010", "1010000011", "1010000100", "1010000101", "1010000110"]},

    {"tipo": "higiene", "codigo_barra": "101001", "codigo": "3002", "nome": "Shampoo", "preco": 8.0, "quantidade": 6, 
     "codigos_barras": ["1010010000", "1010010001", "1010010010", "1010010011", "1010010100", "1010010101"]}
]

limpeza = [
    {"tipo": "limpeza", "codigo_barra": "101010", "codigo": "4001", "nome": "Detergente", "preco": 3.5, "quantidade": 1, 
     "codigos_barras": ["1010100000"]}
]

# Dicionário que mapeia cada tipo de produto para sua respectiva lista
tipos_produtos = {
    "alimento": alimentos,  # Lista de produtos de tipo 'alimento'
    "bebida": bebidas,      # Lista de produtos de tipo 'bebida'
    "higiene": higiene,     # Lista de produtos de tipo 'higiene'
    "limpeza": limpeza      # Nova categoria 'limpeza'
}

produtos_indisponiveis = []
