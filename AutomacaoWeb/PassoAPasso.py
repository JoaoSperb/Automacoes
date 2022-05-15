from selenium import webdriver  #abrir a aba
from selenium.webdriver.common.by import By  # localiza elementos(os itens do site)
from selenium.webdriver.common.keys import Keys  #permite clicar teclas no teclado



navegador = webdriver.Chrome(executable_path=r"C:\Users\lecos\OneDrive\Área de Trabalho\chromedriver.exe")

#link do drive https://drive.google.com/drive/folders/1KmAdo593nD8J9QBaZxPOG1yxHZua4Rtv

#Passo 1 - Entrar no google:
navegador.get("https://www.google.com.br/")

#Passo 2 - Pesquisar a cotação do dolar:
navegador.find_element(By.XPATH,
            '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação do dolar")
#entra na barra de pesquisa e pesquisa 'cotaçao do dolar'
#para copiar o XPATH de algo na pagina, é necessario inspecionar a pagina e clicar numa setinha no canto superior
#esquerdo, e entao clicar em cima do elemento desejado.

navegador.find_element(By.XPATH,
                '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
#Aperta ENTER, apos colocar 'cotaçao do dolar' na barra de pesquisa

cotacao_dolar = navegador.find_element(By.XPATH,
        '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
#o data value é encontrado no inspecionar também, e nem sempre o data-value que sera utilizado aqui


#Passo 3 - Atualizar a cotaçao do dolar:


#Passo 4 - Pesquisar a cotação do euro:
navegador.get("")

#Passo 5 - Atualizar a cotaçao do euro:


#Passo 6 - Pesquisar a cotação da grama do ouro:


#Passo 7 - Atualizar a cotaçao da grama do ouro:

#Passo 8 - Atualizar a base de dados com as novas cotaçoes:



