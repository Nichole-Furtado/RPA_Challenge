from selenium import webdriver as opcoes
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

import pyautogui as espera

planilha = "C:\\Users\\nicho\\PycharmProjects\\Rpa_Challenge_dados\\challenge (2).xlsx" # porque duas barras
df = pd.read_excel(planilha)

navegador = opcoes.Chrome()

navegador.get("https://rpachallenge.com")

espera.sleep(5)

navegador.find_element(By.XPATH, "/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button").click()

#ler linha por linha
for index,row in df.iterrows():

    PrimeiroNome = row['First Name']
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelFirstName"]').send_keys(PrimeiroNome)

    SegundoNome = row['Last Name ']
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelLastName"]').send_keys(SegundoNome)

    Nome_companhia = row['Company Name']
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelCompanyName"]').send_keys(Nome_companhia)

    Tipo_companhia = row['Role in Company']
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelRole"]').send_keys(Tipo_companhia)

    Endereço = row['Address']
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelAddress"]').send_keys(Endereço)

    Email = row['Email']
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelEmail"]').send_keys(Email)

    Número_Telefone = row['Phone Number']
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelPhone"]').send_keys(Número_Telefone)

    navegador.find_element(By.XPATH, "/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input").click()

espera.sleep(10)

print('Enviado com sucesso! :)')
