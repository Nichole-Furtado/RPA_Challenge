# RPA Challenge

Este projeto tem como objetivo automatizar o preenchimento de formulários com base em dados de um arquivo Excel, utilizando Python. Ele foi desenvolvido como um exercício de automação de processos (RPA - Robotic Process Automation).

## 📁 Estrutura do Projeto

- `RPA_Challenge_comPandas.py` – Script principal utilizando a biblioteca **Pandas** para manipulação de dados.
- `ExemploBasico_semPandas.py` – Versão alternativa do script sem uso do **Pandas**, ideal para aprendizado básico.
- `challenge (2).xlsx` – Arquivo Excel contendo os dados a serem utilizados no processo automatizado.
- `.idea/` – Configurações do projeto para o PyCharm (pode ser ignorado se não estiver usando o PyCharm).

## 🚀 Requisitos

- Python 3.7+
- Bibliotecas:
  - `pandas`
  - `openpyxl`
  - `pyautogui`
  - `time` (interna do Python)

Instale as dependências com:
- pip install pandas openpyxl pyautogui

⚙️ Como usar
Abra o site ou aplicação onde o formulário será preenchido.

Certifique-se de que o Excel challenge (2).xlsx está na mesma pasta que os scripts.

Execute o script desejado:
python RPA_Challenge_comPandas.py
O script lerá os dados do Excel e preencherá os campos automaticamente.

📚 Aprendizado

- Este projeto é ótimo para aprender:

- Leitura e manipulação de dados com pandas e openpyxl.

- Automação de tarefas com pyautogui.

- Lógica de repetição e controle de tempo (time.sleep).

📌 Observações
- O pyautogui simula o controle do mouse e do teclado, portanto não mexa no computador durante a execução do script.

Adapte as coordenadas e os tempos de espera conforme o seu ambiente.
