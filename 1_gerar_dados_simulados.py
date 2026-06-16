import pandas as pd
import numpy as np
import os

print("=== 1. GERANDO DADOS SIMULADOS DE CNPJ ===")
os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

num_empresas = 5000
np.random.seed(42)

dados_simulados = {
    'cnpj_basico': np.random.randint(10000000, 99999999, size=num_empresas),
    'nome_fantasia': [f"Empresa Comercial {i}" for i in range(num_empresas)],
    'situacao_cadastral': np.random.choice([2, 3, 4], size=num_empresas, p=[0.95, 0.03, 0.02]),
    'data_inicio_atividade': pd.date_range(start='2010-01-01', end='2024-12-31', periods=num_empresas).strftime('%Y-%m-%d'),
    'cnae_fiscal_principal': np.random.choice([4711302, 4781400, 5611201], size=num_empresas),
    'capital_social': np.random.exponential(scale=150000, size=num_empresas) + 5000,
    'uf': np.random.choice(['RJ', 'SP', 'MG'], size=num_empresas, p=[0.7, 0.2, 0.1]),
    'municipio': np.random.choice(['Rio de Janeiro', 'Niterói', 'Duque de Caxias'], size=num_empresas)
}

df_fake = pd.DataFrame(dados_simulados)
df_fake.loc[df_fake.sample(frac=0.02).index, 'capital_social'] *= 50 

df_fake.to_csv("data/raw/estabelecimento0.csv", sep=';', index=False)
print("Sucesso! Arquivo 'estabelecimento0.csv' criado na pasta data/raw.\n")