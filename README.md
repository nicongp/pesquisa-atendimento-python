# 📊 Pesquisa de Satisfação de Atendimento

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Pesquisa](https://img.shields.io/badge/Pesquisa-Satisfa%C3%A7%C3%A3o-007ACC?style=for-the-badge)

## 🎯 Objetivo do Sistema
Um programa de linha de comando desenvolvido para empresas coletarem dados, projetado para coletar o feedback de atendimento dos clientes e contabilizar os indicadores finais de satisfação de forma automatizada.

## 💻 Linguagem Utilizada
- **Python 3**

## 🧮 Funcionamento e Lógica do Sistema
O sistema utiliza uma estrutura de repetição dinâmica (`while`) que permite ao gestor definir o número de pesquisas que deseja realizar (facilitando a alteração para 10 no momento dos testes ou 50 para a pesquisa completa).

Durante a coleta, o código utiliza estruturas de decisão (`if/elif/else`) para filtrar e contabilizar as opiniões:

- **1 - EXCELENTE:** Soma +1 no contador de satisfação alta (`total_excelente`).
- **2 - BOM:** Opção válida registrada no fluxo de atendimento.
- **3 - RUIM:** Soma +1 no contador de insatisfação (`total_ruim`).
- **Outras opções:** Trata entradas inválidas informando o usuário sem corromper a contagem.

Ao final do laço de repetição, o programa exibe o relatório consolidado com a quantidade total de respostas **EXCELENTE** e **RUIM**.

## 🚀 Como executar o programa
1. Certifique-se de ter o Python instalado na máquina.
2. Abra o terminal na pasta do projeto.
3. Execute o comando:
   ```bash
   python pesquisa.py
