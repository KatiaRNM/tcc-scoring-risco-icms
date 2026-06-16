import pandas as pd

print("=== 3. ENGENHARIA DE ATRIBUTOS (REGRAS DE NEGÓCIO SEFAZ-RJ) ===")
df_empresas = pd.read_csv("data/processed/empresas_rj_filtradas.csv", sep=';')

# Simulação dos dados macroeconômicos oficiais da SEFAZ-RJ por setor (CNAE)
dados_sefaz_setorial = {
    'cnae_fiscal_principal': [4711302, 4781400, 5611201],
    'arrecadacao_media_setor': [500000, 80000, 45000],
    'capital_medio_setor': [2000000, 150000, 90000]
}
df_sefaz = pd.DataFrame(dados_sefaz_setorial)

# Cruzando os dados da Receita com as médias da SEFAZ
df_processado = pd.merge(df_empresas, df_sefaz, on='cnae_fiscal_principal', how='left')

# Criando as variáveis (features) de desvio
df_processado['feature_desvio_capital'] = df_processado['capital_social'] / df_processado['capital_medio_setor']
df_processado['data_inicio_atividade'] = pd.to_datetime(df_processado['data_inicio_atividade'], errors='coerce')
df_processado['feature_idade_anos'] = (pd.Timestamp.now() - df_processado['data_inicio_atividade']).dt.days / 365.25
df_processado.fillna(0, inplace=True)

df_processado.to_csv("data/processed/base_treinamento_score.csv", index=False, sep=';')
print("Sucesso! Variáveis de risco calculadas e salvas.\n")