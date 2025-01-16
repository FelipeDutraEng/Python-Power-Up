# pip install pyautogui
# pip install pandas openpyxl
import pyautogui
from time import sleep

pyautogui.PAUSE = 0.5

# pyautogui.click -> clica
# pyautogui.press -> pressiona um botão
# pyautogui.write -> escreve
# pyautogui.hotkey -> combinação de teclas (ctrl + c)

# Passo 1: Abrir o sistema da empresa


# Apertar a tecla do Windows
pyautogui.press("win")
# Digitar o nome Google Chrome
pyautogui.write("chrome")
# Abrir o Google Chrome
pyautogui.press("enter")
# Entrar no link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
# Acessar o site do sistema
pyautogui.press("enter")
# Pedir pro computador esperar 3 segundos
sleep(1)
 

#Passo 2: Fazer Login
# REALIZAR PONTO DE MELHORIA UTILIZANDO O PYAUTOGUI.LOCATEONSCREEN das abas de login e senha

# Click no campo de login
pyautogui.click(x=2445, y=377)
# Escrever o login
pyautogui.write("felipe.dutra@hotmail.com")
# Click no campo de senha
pyautogui.press("tab")
# Escrever a senha
1234    
pyautogui.write("1234")
# Click no botão de login
pyautogui.press("tab")
pyautogui.press("enter")

# Passo 3: Importar a base de dados dos produtos

import pandas

tabela = pandas.read_csv(r"C:\Users\Felip\OneDrive\Documentos\Engenharia de Dados\Python Power Up\Python Power Up - 1 Automação de Tarefas\produtos.csv")
print(tabela)
sleep(1)

# Passo 4: Cadastrar 1 produto

# Clicar na caixa de texto do código do produto
'''pyautogui.click(x=2434, y=261)
# Escrever o código do produto
pyautogui.write("MOLO000251")
pyautogui.press("tab")
# Escrever marca do produto
pyautogui.write("Logitech")
pyautogui.press("tab")
# Escrever Tipo do produto
pyautogui.write("Mouse")
pyautogui.press("tab")
# Escrever Categoria do produto
pyautogui.write("1")
pyautogui.press("tab")
# Escrever Preço Unitário do produto
pyautogui.write("25.95")
pyautogui.press("tab")
# Escrever Custo do produto
pyautogui.write("6.5")
pyautogui.press("tab")
# Escrever Observações
pyautogui.write("")
pyautogui.press("tab")
# Clicar no botão Enviar
pyautogui.press("enter")

# Subir a tela com Scroll
pyautogui.scroll(10000)'''


# Passo 5: Repetir o passo 4 para todos os produtos da base de dados

for linha in tabela.index: 
    # Clicar na caixa de texto do código do produto
    pyautogui.click(x=2434, y=261)
    # Escrever o código do produto
    codigo = tabela.loc[linha, "codigo"]   
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    # Escrever marca do produto
    marca = tabela.loc[linha, "marca"]  
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    # Escrever Tipo do produto
    tipo = tabela.loc[linha, "tipo"]    
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    # Escrever Categoria do produto
    categoria = tabela.loc[linha, "categoria"]   
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    # Escrever Preço Unitário do produto
    precoUnitario = tabela.loc[linha, "preco_unitario"] 
    pyautogui.write(str(precoUnitario))
    pyautogui.press("tab")
    # Escrever Custo do produto
    custo = tabela.loc[linha, "custo"] 
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    # Escrever Observações
    obs = tabela.loc[linha, "obs"]
    if obs != "nan":
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    # Clicar no botão Enviar
    pyautogui.press("enter")

    # Subir a tela com Scroll
    pyautogui.scroll(10000)

# nan = valor vazio em uma tabela
# Not = Not a Number