from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

navegador = webdriver.Chrome(executable_path=r"C:\Users\lecos\OneDrive\Área de Trabalho\chromedriver.exe")

# link do drive https://drive.google.com/drive/folders/1KmAdo593nD8J9QBaZxPOG1yxHZua4Rtv

# Passo 1 - Entrar no google:
navegador.get("https://www.google.com.br/")

# Passo 2 - Pesquisar a cotação do dolar:
navegador.find_element(By.XPATH,
            '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação do dolar")

navegador.find_element(By.XPATH,
                '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_dolar = navegador.find_element(By.XPATH,
        '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

# Passo 4 - Pesquisar a cotação do euro:
navegador.get("https://www.google.com.br/")

navegador.find_element(By.XPATH,
            '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação do euro")

navegador.find_element(By.XPATH,
                '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_euro = navegador.find_element(By.XPATH,
        '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

# Passo 5 - Pesquisar a cotação da grama do ouro:
navegador.get("https://www.melhorcambio.com/ouro-hoje")
cotacao_ouro = navegador.find_element(By.XPATH,
                                    '//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(',', '.')


# Passo 6  - Atualizar a base de dados com as novas cotaçoes
tabela = pd.read_excel(r"C:\Users\lecos\OneDrive\Área de Trabalho\drive-download-20220515T191250Z-001\Produtos.xlsx")

tabela.loc[tabela["Moeda"] == "Dólar","Cotação"] = float(cotacao_dolar)
#Nas linhas onde moeda == dolar, na coluna cotaçao, o valor muda
tabela.loc[tabela["Moeda"]=="Euro", "Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"]=="Ouro", "Cotação"] = float(cotacao_ouro)

tabela["Preço de Compra"] = tabela['Preço Original'] * tabela['Cotação']
tabela["Preço de Venda"] = tabela['Preço de Compra'] * tabela['Margem']
#Atualizaçoes do preço de compra e do preço de venda

print(tabela)
