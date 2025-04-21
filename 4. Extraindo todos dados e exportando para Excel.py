from selenium import webdriver as opcoes #Para consegue pegar dados do navegador
from selenium.webdriver.common.by import By
import pandas as pd
import pyautogui as espera

navegador = opcoes.Chrome() #criou uma instância com a varíavel navegador para abrir o chrome

navegador.get("https://rpachallengeocr.azurewebsites.net/") # buscou o link informado

elemento = navegador.find_element(By.XPATH, '//*[@id= "tableSandbox"]') #xPath
colunas = elemento.find_elements(By.TAG_NAME, "td")
linhas = elemento.find_elements(By.TAG_NAME, "tr")

df_lista = []

linha = 1 # Contador

i = 1

while i < 4:

    # mesma coisa que i = i +1
    elemento = navegador.find_element(By.XPATH, '//*[@id= "tableSandbox"]')  # xPath

    colunas = elemento.find_elements(By.TAG_NAME, "td")
    linhas = elemento.find_elements(By.TAG_NAME, "tr")
    for linha_Atual in linhas:
        print(linha_Atual.text)
        #    linha = linha + 1 # vai printar na tela e percorrer linha por linha
        df_lista.append(linha_Atual.text)
        linha += 1  # sintaxe mais reduzida

    i += 1

    espera.sleep(2)

    navegador.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()

    espera.sleep(2)
else:
    print('Dados extraídos com sucesso!')


excel = pd.ExcelWriter('DadosAbaSite.xlsx', engine='xlsxwriter')#instalar modulos XlsxWriter
excel.close()

df = pd.DataFrame(df_lista, columns=['#;ID;DueDate'])

excel = pd.ExcelWriter('DadosAbaSite.xlsx', engine='xlsxwriter')

df.to_excel(excel, sheet_name= 'Sheet1', index=False)

excel.close() #atualizado, antes era save, agora close

