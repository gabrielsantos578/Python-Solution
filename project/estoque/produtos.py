# Listas de produtos
alimentos = [
    {"tipo": "alimento", "numero_serie": "001", "nome": "Arroz", "preco": 5.0},
    {"tipo": "alimento", "numero_serie": "002", "nome": "Feijão", "preco": 7.0}
]


bebidas = [
    {"tipo": "bebida", "numero_serie": "003", "nome": "Refrigerante", "preco": 4.0},
    {"tipo": "bebida", "numero_serie": "004", "nome": "Água", "preco": 2.0}
]


higiene = [
    {"tipo": "higiene", "numero_serie": "005", "nome": "Sabonete", "preco": 1.5},
    {"tipo": "higiene", "numero_serie": "006", "nome": "Shampoo", "preco": 8.0}
]


# Dicionário de tipos de produtos para fácil acesso
tipos_produtos = {
    "alimento": alimentos,
    "bebida": bebidas,
    "higiene": higiene
}