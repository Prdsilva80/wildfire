import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset (substitua 'wildfires.csv' pelo caminho do seu arquivo)
df = pd.read_csv('./assets/areaburntbywildfiresbyweeknew.csv')

# Visualize as primeiras linhas do dataset
print(df.head())

# Substitua espaços em branco nos nomes das colunas
df.columns = df.columns.str.strip()

# 1. Análise da área queimada total por ano (usando apenas os anos disponíveis)
anos = ['area burnt by wildfires in 2024', 'burnt by wildfires in 2023', 
        'burnt by wildfires in 2022', 'burnt by wildfires in 2021', 
        'burnt by wildfires in 2020', 'area burnt by wildfires in 2019', 
        'a burnt by wildfires in 2018', 'area burnt by wildfires in 2017', 
        'area burnt by wildfires in 2016', 'area burnt by wildfires in 2015', 
        'area burnt by wildfires in 2014', 'area burnt by wildfires in 2013', 
        'area burnt by wildfires in 2012']

# Limpe os nomes das colunas (para remover espaços extras)
df.columns = df.columns.str.strip()

# Calcular a área queimada total para cada ano
total_area_queimada = df[anos].sum()

# Criar um DataFrame para facilitar a visualização
df_area_queimada = pd.DataFrame({
    'Ano': [int(col[-4:]) for col in anos],  # Extrai os anos dos nomes das colunas
    'Área Queimada (hectares)': total_area_queimada.values
})

# Ordenar os dados pelo ano
df_area_queimada = df_area_queimada.sort_values('Ano')

# Plotar a área queimada por ano
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_area_queimada, x='Ano', y='Área Queimada (hectares)', marker='o', color='r')
plt.title('Área Total Queimada por Incêndios Florestais por Ano')
plt.xlabel('Ano')
plt.ylabel('Área Queimada (hectares)')
plt.grid(True)
plt.tight_layout()
plt.show()