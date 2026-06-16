import pandas as pd

print("=== 2. FILTRANDO EMPRESAS ATIVAS DO RIO DE JANEIRO ===")
df_bruto = pd.read_csv("data/raw/estabelecimento0.csv", sep=';')

# Filtrando apenas empresas do RJ e com situação cadastral igual a 2 (Ativa)
df_rj = df_bruto[(df_bruto['uf'] == 'RJ') & (df_bruto['situacao_cadastral'] == 2)]

df_rj.to_csv("data/processed/empresas_rj_filtradas.csv", index=False, sep=';')
print(f"Sucesso! Encontradas {len(df_rj)} empresas ativas no Rio de Janeiro.")
print("Arquivo guardado em data/processed/empresas_rj_filtradas.csv.\n")