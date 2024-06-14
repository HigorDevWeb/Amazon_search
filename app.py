from flask import Flask, request, render_template
from amazon_scraper import init_browser, search_amazon, get_search_results, extract_product_info
from db_manager import init_db, insert_data_into_db

# Inicializa a aplicação Flask e define a pasta onde estão os templates
app = Flask(__name__, template_folder='templates')

# Rota principal que renderiza o template index.html
@app.route('/')
def index():
    return render_template('index.html')

# Rota para processar a busca de produtos na Amazon
@app.route('/search', methods=['POST'])
def search():
    # Obtém o termo de busca do formulário enviado pelo método POST
    search_query = request.form['query']
    
    # Inicializa o navegador e realiza a busca na Amazon
    browser = init_browser()
    search_amazon(browser, search_query)
    
    # Obtém os resultados da busca na Amazon
    items = get_search_results(browser)
    
    # Inicializa o banco de dados SQLite e prepara para inserção de dados
    conn, c = init_db()
    
    # Lista para armazenar os produtos encontrados
    products = []
    
    # Itera sobre os itens encontrados na busca
    for item in items:
        # Extrai informações do produto a partir do elemento HTML
        title, price, link, img = extract_product_info(item)
        
        # Insere os dados do produto no banco de dados SQLite
        insert_data_into_db(conn, c, title, price, link, img)
        
        # Adiciona as informações do produto à lista de produtos
        products.append({
            'title': title,
            'price': price,
            'link': link,
            'img': img
        })
    
    # Fecha a conexão com o banco de dados SQLite
    conn.close()
    
    # Fecha o navegador
    browser.quit()
    
    # Renderiza o template results.html passando a lista de produtos encontrados
    return render_template('results.html', products=products)

# Verifica se o script está sendo executado diretamente e inicia o servidor Flask em modo de depuração
if __name__ == '__main__':
    app.run(debug=True)
