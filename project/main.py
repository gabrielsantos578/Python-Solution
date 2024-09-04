from utilitarios import menu_principal



# Função principal que inicializa o programa
def main():
    menu_principal.exibir_interface()  # Chama a interface principal do menu


# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()  # Executa a função principal





"""
--------------------------------------------------------------------------------------------------------------------

Participantes:

    > Marco Antônio Alcindo Gitti

    > Gabriel Machado dos Santos



* Aplicação: Sistema de Gestão de Processos de Venda de Supermercado *


# Problema Enfrentado: 
    
    > O cliente enfrenta diversos desafios em seu sistema de gestão de vendas do supermercado. Entrando em contato com o mesmo, foi levantando os seguintes problemas e requisitos:

    1. Gestão de Processos de Venda no Caixa:

        > O cliente precisa de uma solução para gerenciar eficientemente o processo de venda no caixa. O sistema atual não proporciona uma forma automatizada e precisa de realizar e 
        registrar as vendas, o que resulta em processos manuais demorados e suscetíveis a erros.

    2. Identificação e Contagem de Produtos:

        > O cliente deseja que o sistema utilize a leitura de códigos de barras para identificar automaticamente os produtos. O sistema deve ser capaz de adicionar os itens à venda 
        em andamento, contabilizando a quantidade e o valor de cada produto.

    3. Geração de Recibos e Armazenamento de Dados:

        > É essencial para o cliente que o sistema gere recibos detalhados após cada venda e que esses dados sejam armazenados para análise administrativa. O sistema existente não 
        oferecia um meio eficiente de gerar e armazenar recibos, dificultando a análise de vendas e o acompanhamento financeiro, bem como na gestão logística.

    4. Seções para Setores Administrativo e Logístico:

        > O cliente solicitou que fossem criadas seções distintas para os setores administrativo e logístico. A equipe administrativa precisa acessar relatórios de faturamento e dados de 
        vendas, enquanto o setor logístico necessita de informações sobre o estoque, incluindo produtos disponíveis e indisponíveis.

        
# Solução Proposta:

    > Para resolver os problemas enfrentados pelo cliente, propomos uma aplicação com as seguintes funcionalidades e melhorias:

    1. Gestão Automatizada de Vendas:

        > Desenvolvemos um módulo que permite a realização de vendas diretamente no caixa através da leitura de códigos de barras dos produtos. O sistema identifica 
        automaticamente o produto correspondente, adiciona-o aos itens da venda, e calcula a quantidade e o valor total dos produtos selecionados. Essa automação reduz o tempo de 
        processamento e minimiza erros.

    2. Interface para o Setor Administrativo:
    
        > Criamos uma seção dedicada ao setor administrativo que fornece ferramentas para acessar relatórios de faturamento, visualizar recibos e analisar detalhes das vendas. Esse módulo 
        permite ao administrador revisar dados financeiros, acompanhar o desempenho das vendas e tomar decisões informadas com base nas informações disponíveis.

    3. Interface para o Setor Logístico:

        > Desenvolvemos uma seção específica para o setor logístico, oferecendo uma visão clara do estoque de produtos. A interface permite monitorar itens disponíveis e indisponíveis, 
        gerenciar reabastecimentos e otimizar o controle de inventário. Essa funcionalidade assegura que o setor logístico tenha acesso às informações necessárias para manter o estoque em 
        níveis adequados.

--------------------------------------------------------------------------------------------------------------------
"""