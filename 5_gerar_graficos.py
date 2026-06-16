import os
import pandas as pd
import matplotlib.pyplot as plt

# Criar pasta para salvar os gráficos se não existir
os.makedirs("data/outputs", exist_ok=True)

print("=== 5. GERANDO GRÁFICOS DO MODELO DE RISCO FISCAL ===")

# Lendo os resultados gerados pelo modelo
df = pd.read_csv("data/processed/resultado_scoring_fiscal.csv", sep=';')

# Definindo as cores padrão do TCC
cores = {'Baixo': '#2ecc71', 'Médio': '#f1c40f', 'Alto': '#e74c3c'}

# --- GRÁFICO 1: DISTRIBUIÇÃO DAS CLASSES DE RISCO ---
plt.figure(figsize=(8, 5))
contagem = df['classificacao_risco'].value_counts().reindex(['Baixo', 'Médio', 'Alto'])
contagem.plot(kind='bar', color=[cores['Baixo'], cores['Médio'], cores['Alto']], edgecolor='black')

plt.title('Distribuição de Empresas por Classificação de Risco Fiscal', fontsize=12, fontweight='bold')
plt.xlabel('Classificação de Risco', fontsize=10)
plt.ylabel('Quantidade de Empresas', fontsize=10)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('data/outputs/grafico_distribuicao_risco.png', dpi=300)
plt.close()
print("-> Gráfico 1 salvo em 'data/outputs/grafico_distribuicao_risco.png'")

# --- GRÁFICO 2: DISPERSÃO (IDADE VS DESVIO DE CAPITAL) ---
plt.figure(figsize=(10, 6))

for classe in ['Baixo', 'Médio', 'Alto']:
    sub_df = df[df['classificacao_risco'] == classe]
    plt.scatter(sub_df['feature_idade_anos'], sub_df['feature_desvio_capital'], 
                color=cores[classe], label=f'Risco {classe}', alpha=0.7, s=40)

plt.title('Detecção de Anomalias Fiscais: Idade vs. Desvio de Capital Social', fontsize=12, fontweight='bold')
plt.xlabel('Idade da Empresa (Anos)', fontsize=10)
plt.ylabel('Desvio de Capital (Relação com a Média do Setor SEFAZ)', fontsize=10)
plt.legend(title="Classificação do Modelo")
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('data/outputs/grafico_dispersao_anomalias.png', dpi=300)
plt.close()
print("-> Gráfico 2 salvo em 'data/outputs/grafico_dispersao_anomalias.png'")

print("\n=== TODOS OS GRÁFICOS GERADOS COM SUCESSO! ===")