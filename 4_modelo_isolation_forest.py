import subprocess
import sys

print("=== Verificando e Instalando a biblioteca scikit-learn automáticamente ===")
try:
    import sklearn
except ModuleNotFoundError:
    # Força a instalação diretamente no Python que o Spyder está usando
    subprocess.check_call([sys.executable, "-m", "pip", "install", "scikit-learn", "--break-system-packages"])
    print("Biblioteca instalada com sucesso!")

# Agora o código do seu modelo roda perfeitamente:
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

print("=== 4. EXECUTANDO MACHINE LEARNING (ISOLATION FOREST) ===")
df_modelo = pd.read_csv("data/processed/base_treinamento_score.csv", sep=';')

features = ['feature_desvio_capital', 'feature_idade_anos', 'capital_social']
X = df_modelo[features]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

modelo = IsolationForest(contamination=0.05, random_state=42)
modelo.fit(X_scaled)

scores_brutos = modelo.decision_function(X_scaled)
df_modelo['score_risco_fiscal'] = 100 * (1 - (scores_brutos - scores_brutos.min()) / (scores_brutos.max() - scores_brutos.min()))

df_modelo['classificacao_risco'] = pd.cut(df_modelo['score_risco_fiscal'], bins=[0, 30, 70, 100], labels=['Baixo', 'Médio', 'Alto'])
df_resultado = df_modelo.sort_values(by='score_risco_fiscal', ascending=False)

df_resultado.to_csv("data/processed/resultado_scoring_fiscal.csv", index=False, sep=';')

print("\n=== MODELO EXECUTADO COM SUCESSO! ===")
print("Top 5 Empresas com Maior Risco de Sonegação Fiscal Detectadas no RJ:")
print(df_resultado[['cnpj_basico', 'nome_fantasia', 'score_risco_fiscal', 'classificacao_risco']].head())