# %%

import pandas as pd
# %%
df = pd.read_csv("../Data/pedido.csv")
df
# %%

colunas = ["idPedido", "descUF"]

df[colunas]
# %%
colunas = [
    "idPedido",
    "descUF",
    "flKetchup",
    "txtRecado",
    "dtPedido",
]

df = df[colunas]
# %%
df_sample = df.sample(100)
df_sample
# %%
df_sample.iloc[0]
# %%
df_sample.loc[706]