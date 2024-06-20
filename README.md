# Amazon Products API

Esta é uma API simples para gerenciar produtos da Amazon, construída com Flask e SQLite.

## Descrição

A API permite buscar produtos por ID e adicionar novos produtos ao banco de dados. A comunicação é feita via endpoints RESTful.

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/amazon-products-api.git
    cd amazon-products-api
    ```

2. Crie um ambiente virtual e instale as dependências:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Certifique-se de que o arquivo `amazon_products.db` está na pasta do projeto.

## Uso

### Rodando a API

Para iniciar o servidor Flask, execute:
```bash
flask run
Endpoints
GET /product/<product_id>
Busca um produto pelo ID.

Parâmetros de URL: product_id - ID do produto
Resposta de Sucesso: 200 OK
json
Copy code
{
    "id": 1,
    "title": "Example Product",
    "price": "$19.99",
    "link": "http://example.com/product",
    "image": "http://example.com/image.jpg"
}
Resposta de Erro: 404 Not Found
json
Copy code
{
    "error": "Product not found"
}
POST /product
Adiciona um novo produto.

Corpo da Requisição:
json
Copy code
{
    "title": "New Product",
    "price": "$29.99",
    "link": "http://example.com/new-product",
    "image": "http://example.com/new-image.jpg"
}
Resposta de Sucesso: 201 Created
json
Copy code
{
    "product_id": 2
}
Resposta de Erro: 400 Bad Request
json
Copy code
{
    "error": "Product could not be added"
}
Estrutura do Projeto
bash
Copy code
amazon-products-api/
├── app.py              # Arquivo principal da aplicação Flask
├── db_manager.py       # Gerenciamento do banco de dados SQLite
├── amazon_products.db  # Banco de dados SQLite com a tabela 'products'
└── requirements.txt    # Lista de dependências do projeto
Contribuição
Faça um fork do projeto
Crie uma branch para sua feature (git checkout -b feature/nova-feature)
Commit suas mudanças (git commit -am 'Adiciona nova feature')
Envie para o branch (git push origin feature/nova-feature)
Abra um Pull Request
Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

less
Copy code

Este README oferece uma visão geral do projeto, instruções de instalação e uso, além de informações 
