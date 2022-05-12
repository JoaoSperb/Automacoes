import pyautogui
import pyperclip
import time
import pandas

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
time.sleep(8)

# Quarto passo: Importa a base de dados para o Python

# Quinto passo: Calcular os indicadores

# Sexto passo: Enviar emails para a diretoria
