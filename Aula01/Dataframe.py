# %%
import pandas as pd
# %%

data = {
    "nome": ["Matheus", "Julia", "Felipe", "José", "Sandra","Julio"],
    "idade": [24, 24, 28, 32, 55, 59],
    "cor": ["roxo", "azul", "vermelho", "verde", "rosa", "amarelo"]
}

df = pd.DataFrame(data)
df
# %%
df["idade"]
# %%
df.describe()
# %%
df.info()
# %%
df["idade"].mean()