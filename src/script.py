# Bibliotecas para manipulação de dados
import calendar

import numpy as np  # Biblioteca fundamental para computação científica e manipulação de arrays e matrizes.
import pandas as pd  # Biblioteca principal para manipulação de dados em tabelas (DataFrames).

# Bibliotecas para análise exploratória de dados
# from pandas_profiling import ProfileReport  # Gera relatórios automáticos de análise exploratória dos dados.

# Bibliotecas para visualização de dados
import seaborn as sns  # Biblioteca para visualizações estatísticas e gráficos bonitos.
import matplotlib.pyplot as plt  # Biblioteca principal para criação de gráficos e visualizações personalizáveis.

# Bibliotecas para modelagem e pré-processamento de dados
from sklearn import metrics  # Contém funções para avaliar o desempenho de modelos de aprendizado de máquina.
from sklearn.pipeline import Pipeline  # Facilita a criação de pipelines de transformação e modelagem.
from sklearn.impute import SimpleImputer  # Preenche valores ausentes em dados.
from sklearn.compose import ColumnTransformer  # Aplica transformações em subconjuntos de colunas.
from sklearn.preprocessing import scale, StandardScaler, OneHotEncoder, OrdinalEncoder  # Técnicas de transformação de dados.

# 01 Trazer os dados.
getData = pd.read_csv("C:/Users/danie/PycharmProjects/e-commerce/data/data.csv", sep=",", encoding="ISO-8859-1")
pd.set_option('display.max_columns', None)  # Exibe todas as colunas.
print(getData.head())
print(getData.describe())

# 02 Tratamentos dos dados.
print(f'Quantidade de dados faltando no CustomerID: {getData["CustomerID"].isna().sum()}')
getData = getData.dropna(subset=["CustomerID"])
print(f'Quantidade de dados faltando no CustomerID: {getData["CustomerID"].isna().sum()}')

# 2.1 Preços unitários e quantidade de produtos iguais ou inferior a 0.

# 2.1 Para verificar se existem valores nulos ou menores que zero
getData[getData['UnitPrice'].isnull() | (getData['UnitPrice'] < 0)]
getData[getData['Quantity'].isnull() | (getData['Quantity'] < 0)]

# 2.1 Para filtrar o dataset para conter apenas preços maiores que zero.
getData = getData[getData['UnitPrice'] > 0]

# 2.1  Para filtrar o dataset para conter apenas quantidade maiores que zero.
getData = getData.query("Quantity > 0")

# 2.2 Verifique se existem linhas duplicadas.
print(f"Quantidades de linhas duplicadas: {getData.duplicated().sum()}")
getData = getData.drop_duplicates()
print(f"Quantidades de linhas duplicadas: {getData.duplicated().sum()}")

# 2.3 Tipos de dados da coluna.
print(getData.info())
getData = getData.astype({'CustomerID': 'int'}).assign(InvoiceDate = pd.to_datetime(getData['InvoiceDate']))

print(getData.info())

# 2.4 Tratando os outliers.
# Identificar os outliers com quantidade superior a 10.000 e preço unitário maior que 5.000.
outliers = getData.query("Quantity > 10.000 and UnitPrice > 5.000")
# Verificando os outliers.
print(outliers)

# Remover os outliers do dataset
getData = getData.query("not (Quantity > 10.000 and UnitPrice > 5.000)")

# Verificar se os outliers foram removidos.
print(getData.info())

# 2.5 Crie uma coluna adicional.
getData['PrecoTotalDaCompra'] = getData['UnitPrice'] * getData['Quantity']

# 2.6 Calcular a data da última compra
last_purchase_date = getData['InvoiceDate'].max()

# Calcular a recência para cada cliente
getData['Recency'] = (last_purchase_date - getData['InvoiceDate']).dt.days

# Exibir o dataframe com a recência
print(getData[['CustomerID', 'InvoiceDate', 'Recency']])


# 3 Plotando gráficos

# Plotando Gráfico de Paises
top10Paises = getData.groupby('Country').agg({'PrecoTotalDaCompra': 'sum'})
top10Paises = top10Paises.sort_values(by ='PrecoTotalDaCompra', ascending = False).head(10)

plt.figure(figsize = (10,6))
sns.barplot(x = top10Paises.index, y = top10Paises['PrecoTotalDaCompra'], hue = top10Paises.index, legend = False)

plt.title('Top 10 Países com Maior Preço Total da Compra', fontsize = 14)
plt.xlabel('País', fontsize = 12)
plt.ylabel('Preço Total da Compra', fontsize = 12)
plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()

# Plotando Gráfico De Produtos
top10Produtos = getData.groupby('Description').agg({'PrecoTotalDaCompra': 'sum'})
top10Produtos = top10Produtos.sort_values(by = 'PrecoTotalDaCompra', ascending = False).head(10)

plt.figure(figsize = (10,6))
sns.barplot(x = top10Produtos.index, y = top10Produtos['PrecoTotalDaCompra'], hue = top10Produtos.index, legend=False)

plt.title('Top 10 Produtos mais Vendidos.')
plt.xlabel('Produtos', fontsize = 12)
plt.ylabel('Preço Total da Compra', fontsize = 12)
plt.xticks(rotation = 65)
plt.tight_layout()
plt.show()

# Plotando Gráfico do Valor de venda total por mês
getData['Mes'] = getData["InvoiceDate"].dt.month
valorDeVendaPorMes = getData.groupby('Mes').agg({'PrecoTotalDaCompra': 'sum'})

plt.figure(figsize = (14,10))
sns.barplot(x = valorDeVendaPorMes.index, y = valorDeVendaPorMes['PrecoTotalDaCompra'], hue = valorDeVendaPorMes.index, legend = False)
plt.title('Venda Total por Mês')
plt.xlabel("Meses", fontsize = 12)
plt.ylabel("Valor Total por Mês", fontsize = 12)
plt.xticks(rotation = 0)
plt.tight_layout
plt.show()

# Plotando o gráfico
top10MesEPais = getData.groupby(['Mes', 'Country']).agg({'PrecoTotalDaCompra': 'sum'}).reset_index()
top10MesEPais = top10MesEPais.sort_values(by='PrecoTotalDaCompra', ascending=False).head(10)
top10MesEPais['MesPais'] = top10MesEPais['Mes'].astype(str) + ' - ' + top10MesEPais['Country']

plt.figure(figsize=(12, 8))
sns.barplot(x='MesPais', y='PrecoTotalDaCompra', hue='Country', data=top10MesEPais)
plt.title('Venda Total Por Mês e País')
plt.xlabel("Mês e País", fontsize=12)
plt.ylabel('Valor Total', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()