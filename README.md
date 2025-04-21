# RPA Automation Challenge - Coleta de Dados com Selenium

Este repositório contém uma série de scripts Python desenvolvidos para automatizar a coleta de dados da tabela disponível no site [RPA Challenge OCR](https://rpachallengeocr.azurewebsites.net/). A automação foi feita utilizando Selenium para navegação e Pandas com XlsxWriter para exportação em Excel.

## 📁 Scripts Disponíveis

| Script                                                  | Descrição                                                                 |
|----------------------------------------------------------|---------------------------------------------------------------------------|
| 1. Extraindo_dados_tabela.py                             | Extrai dados simples da tabela HTML e imprime no terminal.               |
| 2. Extraindo dados e Exportando para a Tabela.py         | Extrai os dados da tabela e exporta em um arquivo Excel.                 |
| 3. Extraindo Dados de Todas as Abas.py                   | Automatiza a extração considerando várias abas de dados, se aplicável.   |
| 4. Extraindo todos dados e exportando para Excel.py      | Versão mais completa, exportando todos os dados em um único Excel final. |

## 🔧 Tecnologias Utilizadas

- Python 3.8+
- Selenium
- Pandas
- XlsxWriter
- ChromeDriver

## 📌 Requisitos

- Google Chrome instalado
- ChromeDriver compatível com sua versão do Chrome
- Python 3 instalado

## ▶️ Como Executar

1. Clone o repositório e acesse a pasta:


git clone https://github.com/seu-usuario/RPA--Automation-Challenge.git
cd RPA--Automation-Challenge-main

## 🧠 Explicação Técnica
Selenium: usado para abrir o navegador, acessar a URL e capturar os dados da tabela HTML.

Pandas: utilizado para estruturar os dados em DataFrames.

XlsxWriter: exporta os DataFrames diretamente para arquivos .xlsx.

Cada linha da tabela é capturada com find_elements(By.TAG_NAME, "tr"), e os dados são coletados via .text.

## 💡 Observações
O ChromeDriver precisa estar no PATH ou na mesma pasta dos scripts para funcionar corretamente.

Para casos onde os dados da tabela são exibidos por abas ou páginas, o script 3.Extraindo Dados de Todas as Abas.py trata da navegação entre elas.


