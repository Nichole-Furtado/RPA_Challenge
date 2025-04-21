from selenium import webdriver as opcoes #Para consegue pegar dados do navegador
from selenium.webdriver.common.by import By
import pandas as pd

navegador = opcoes.Chrome() #criou uma instância com a varíavel navegador para abrir o chrome

navegador.get("https://rpachallengeocr.azurewebsites.net/") # buscou o link informado

elemento = navegador.find_element(By.XPATH, '//*[@id= "tableSandbox"]') #xPath
colunas = elemento.find_elements(By.TAG_NAME, "td")
linhas = elemento.find_elements(By.TAG_NAME, "tr")

df_lista = []

linha = 1 # Contador
for linha_Atual in linhas:
    print(linha_Atual.text)
#    linha = linha + 1 # vai printar na tela e percorrer linha por linha
    df_lista.append(linha_Atual.text)
    linha += 1 # sintaxe mais reduzida

excel = pd.ExcelWriter('DadoSite.xlsx', engine='xlsxwriter')#instalar modulos XlsxWriter
excel.close()

df = pd.DataFrame(df_lista, columns=['Dados'])

excel = pd.ExcelWriter('DadoSite.xlsx', engine='xlsxwriter')

df.to_excel(excel, sheet_name= 'Sheet1', index=False)

excel.close() #atualizado, antes sabe, agora close

