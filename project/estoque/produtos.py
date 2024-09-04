# Listas de produtos com detalhes como tipo, código de barras binário, código, nome, preço, quantidade e números de série
alimentos = [
    {"tipo": "alimento", "codigo_barra": "100100", "codigo": "1001", "nome": "Arroz", "preco": 5.0, "quantidade": 10, 
     "codigos_barras": ["10010010", "10010001", "10010000", "10010011", "10010001", "10010010", "10010000", "10010001", "10010010", "10010011"]},  # Produto 1
    
    {"tipo": "alimento", "codigo_barra": "100101", "codigo": "1002", "nome": "Feijão", "preco": 7.0, "quantidade": 8, 
     "codigos_barras": ["10010100", "10010101", "10010110", "10010111", "10010100", "10010101", "10010110", "10010111"]}  # Produto 2
]


bebidas = [
    {"tipo": "bebida", "codigo_barra": "100110", "codigo": "2001", "nome": "Refrigerante", "preco": 4.0, "quantidade": 5, 
     "codigos_barras": ["10011000", "10011001", "10011010", "10011011", "10011000"]},  # Produto 1
    
    {"tipo": "bebida", "codigo_barra": "100111", "codigo": "2002", "nome": "Água", "preco": 2.0, "quantidade": 12, 
     "codigos_barras": ["10011100", "10011101", "10011110", "10011111", "10011100", "10011101", "10011110", "10011111", "10011100", "10011101", "10011110", "10011111"]}  # Produto 2
]


higiene = [
    {"tipo": "higiene", "codigo_barra": "101000", "codigo": "3001", "nome": "Sabonete", "preco": 1.5, "quantidade": 7, 
     "codigos_barras": ["10100000", "10100001", "10100010", "10100011", "10100000", "10100001", "10100010"]},  # Produto 1
    
    {"tipo": "higiene", "codigo_barra": "101001", "codigo": "3002", "nome": "Shampoo", "preco": 8.0, "quantidade": 6, 
     "codigos_barras": ["10100100", "10100101", "10100110", "10100111", "10100100", "10100101"]}  # Produto 2
]


# Dicionário que mapeia cada tipo de produto para sua respectiva lista
tipos_produtos = {
    "alimento": alimentos,  # Lista de produtos de tipo 'alimento'
    "bebida": bebidas,      # Lista de produtos de tipo 'bebida'
    "higiene": higiene      # Lista de produtos de tipo 'higiene'
}
