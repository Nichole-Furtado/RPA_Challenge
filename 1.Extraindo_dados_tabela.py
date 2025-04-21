from selenium import webdriver as opcoes #Para consegue pegar dados do navegador
from selenium.webdriver.common.by import By

navegador = opcoes.Chrome() #criou uma instância com a varíavel navegador para abrir o chrome

navegador.get("https://rpachallengeocr.azurewebsites.net/") # buscou o link informado

elemento = navegador.find_element(By.XPATH, '//*[@id= "tableSandbox"]') #xPath
colunas = elemento.find_elements(By.TAG_NAME, "tr")
linhas = elemento.find_elements(By.TAG_NAME, "td")

linha = 1 # Contador
for linha_Atual in linhas:
#    linha = linha + 1 # vai printar na tela e percorrer linha por linha
    linha =+ 1 # sintaxe mais reduzida
    print(elemento.text)
