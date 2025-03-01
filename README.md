# Análise de Dados de E-Commerce

Este projeto tem como objetivo realizar uma análise exploratória e gerar insights valiosos a partir de um conjunto de dados de e-commerce. Utilizando técnicas de pré-processamento, visualização e métricas de RFM (Recência, Frequência e Monetário), o projeto ajuda a entender o comportamento dos clientes e as tendências de compra. 

## Visão Geral

O conjunto de dados contém informações sobre as transações realizadas em uma plataforma de e-commerce, incluindo detalhes sobre os produtos comprados, os clientes, as faturas e os valores das compras. A análise realiza as seguintes etapas:

1. **Pré-processamento dos dados**: Limpeza, tratamento de dados faltantes, outliers e formatação de colunas.
2. **Análise exploratória**: Exibição de gráficos que mostram as vendas por país, produto, mês e combinação de mês e país.
3. **Cálculo de RFM**: Determinação da Recência, Frequência e Monetário de cada cliente, utilizando suas transações.
4. **Visualizações**: Geração de gráficos interativos e informativos para representar os resultados.

## Tecnologias Utilizadas

- **Pandas**: Para manipulação e análise de dados (DataFrames).
- **NumPy**: Para operações matemáticas e manipulação de arrays.
- **Seaborn**: Para a criação de gráficos estáticos e interativos.
- **Matplotlib**: Para visualizações personalizáveis.
- **Scikit-learn**: Para técnicas de pré-processamento e modelagem (caso necessário).

## Estrutura do Projeto

### 1. **Carregamento e Inspeção dos Dados**

Os dados são carregados de um arquivo CSV, e é realizada uma análise inicial para verificar as primeiras linhas e estatísticas dos dados.

```python
getData = pd.read_csv("C:/Users/danie/PycharmProjects/e-commerce/data/data.csv", sep=",", encoding="ISO-8859-1")
print(getData.head())
print(getData.describe())
