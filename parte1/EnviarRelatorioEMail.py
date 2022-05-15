import pyautogui
import pyperclip
import time
import pandas as pd

pyautogui.PAUSE = 0.5

# banco de dados utilizado: https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing

#  Primeiro passo: entrar no sistema da empresa.
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing')
pyautogui.hotkey('ctrl', "v")
pyautogui.press('enter')

time.sleep(3)

# Segundo passo: Navegar no sistema e encontrar a base de dados.
# para conseguir descobrir a posiçao onde seu mouse está, é utilizado o comando pyautogui.position(), ele mostrará aonde seu mouse esta no
# momento em que o programa for executado
pyautogui.click(x=484, y=383, clicks = 2)
time.sleep(3)

# Terceiro passo: Exportar/Fazer download da Base de Dados
pyautogui.click(x=493, y=477)#clica no arquivo
pyautogui.click(x=1673, y=235)#clica nos tres  pontos
pyautogui.click(x=1410, y=783)#clica para baixar o  arquivo
time.sleep(6)
pyautogui.click(x=1910, y=992)

# Quarto passo: Importa a base de dados para o Python
tabela = pd.read_excel(r"C:\Users\lecos\Downloads\Vendas - Dez.xlsx")

# Quinto passo: Calcular os indicadores
#faturamento = soma da coluna valor final
faturamento = tabela["Valor Final"].sum()
#quantidade de produtos = soma da coluna quantidade
quantidade = tabela["Quantidade"].sum()

# Sexto passo: Enviar emails para a diretoria
#Abrir o email
pyautogui.hotkey('ctrl','t')
pyperclip.copy('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
time.sleep(5)

#clicar em escrevre
pyautogui.click(x=114, y=248)
#escrver o assunto
pyautogui.write('jgbrsperb@gmail.com')
pyautogui.press('tab')
pyautogui.press('tab')
time.sleep(2)
pyautogui.write('Faturamento e quantidade total de vendas.')
pyautogui.press('tab')
#escreve o corpo do email
texto= f""" Prezado,bom dia
o faturamento de ontem foi de:{faturamento} 
A quantidade de produtos  vendida foi de: {quantidade}
"""
pyautogui.write(texto)
time.sleep(2)
#enviar o email
pyautogui.click(x=1197, y=968)


