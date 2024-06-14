from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # Importa WebDriverWait para esperas explícitas
from selenium.webdriver.support import expected_conditions as EC  # Importa expected_conditions para condições esperadas

def init_browser():
    # Inicializa o navegador Firefox
    browser = webdriver.Firefox()
    browser.get('https://www.amazon.com.br')  # Abre o site da Amazon Brasil
    return browser  # Retorna a instância do navegador

def extract_product_info(item):
    # Extrai informações de um item de produto na página de resultados
    title = item.find_element(By.TAG_NAME, 'h2').text  # Extrai o título do produto
    price = ""
    link = item.find_element(By.CLASS_NAME, 'a-link-normal').get_attribute('href')  # Extrai o link do produto

    try:
        # Tenta extrair o preço do produto se disponível
        price = item.find_element(By.CLASS_NAME, 'a-price').text.replace('\n', '.')  
    except:
        pass

    try:
        # Tenta extrair a URL da imagem do produto se disponível
        img = item.find_element(By.CLASS_NAME, 's-image').get_attribute('src')  
    except:
        pass

    return title, price, link, img  # Retorna as informações do produto: título, preço, link e imagem

def search_amazon(browser, search_query):
    # Realiza a busca de um produto na Amazon
    try:
        # Aguarda até que o campo de busca esteja presente na página
        search_box = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, 'twotabsearchtextbox'))
        )
        search_box.send_keys(search_query)  # Insere o termo de busca no campo de busca
        search_box.send_keys(Keys.ENTER)  # Simula a tecla Enter para iniciar a busca
    except Exception as e:
        print(f"Erro ao tentar buscar o elemento de pesquisa: {e}")

def get_search_results(browser):
    # Obtém os resultados da busca na Amazon
    try:
        # Aguarda até que o contêiner principal dos resultados esteja presente na página
        main_container = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.s-main-slot.s-result-list.s-search-results.sg-row'))
        )
        # Retorna todos os elementos de resultado de busca encontrados
        return main_container.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')
    except Exception as e:
        print(f"Erro ao tentar buscar os resultados: {e}")
        return []

# O código acima define funções para inicializar o navegador, extrair informações de produtos, realizar buscas e obter resultados de busca na Amazon.
