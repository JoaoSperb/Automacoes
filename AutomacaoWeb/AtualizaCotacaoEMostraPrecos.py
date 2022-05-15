from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



navegador = webdriver.Chrome(executable_path=r"C:\Users\lecos\OneDrive\Área de Trabalho\chromedriver.exe")

#link do drive https://drive.google.com/drive/folders/1KmAdo593nD8J9QBaZxPOG1yxHZua4Rtv

#Passo 1 - Entrar no google:
navegador.get("https://www.google.com.br/")

#Passo 2 - Pesquisar a cotação do dolar:
navegador.find_element(By.XPATH,
            '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação do dolar")

navegador.find_element(By.XPATH,
                '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_dolar = navegador.find_element(By.XPATH,
        '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

#Passo 4 - Pesquisar a cotação do euro:
navegador.get("https://www.google.com.br/")

navegador.find_element(By.XPATH,
            '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação do euro")

navegador.find_element(By.XPATH,
                '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_euro = navegador.find_element(By.XPATH,
        '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

#Passo 5 - Pesquisar a cotação da grama do ouro:
navegador.get("https://www.melhorcambio.com/ouro-hoje")
cotacao_ouro = navegador.find_element(By.XPATH,
                                    '//*[@id="comercial"]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(',', '.')
print(valor_ouro)
#Passo 6  - Atualizar a base de dados com as novas cotaçoes:



