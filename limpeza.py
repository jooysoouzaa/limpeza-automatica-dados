import pandas as pd
import os

# Cria pasta de saída, se não existir
os.makedirs("output", exist_ok=True)

# Le os dados brutos
df = pd.read_csv("data/dados.csv")

# Faz umalimpeza básica
df = df.drop_duplicates()
df = df.dropna(how="all")  # remove linhas completamente vazias

# Exporta os dados limpos
df.to_csv("output/dados_limpos.csv", index=False)

print("A limpeza foi concluída com sucesso.")
