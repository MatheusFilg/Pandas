# %% 
import pandas as pd
import numpy as np
# %%
df = pd.read_csv("../Data/produto.csv")
df
# %%
df.info()
# %%
df["PrecoAjustado"] = (df["vlPreco"] * 1.09).round(2)
df
# %%
df["txAjuste(%)"] = (100 * (df["PrecoAjustado"] / df["vlPreco"] -1)).round(2)
df
# %%
df.drop(columns=["txAjuste"]) #retornando um novo df
# %%
df = df.drop(columns=["txAjuste"])
df
# %%

df["logTxAjuste"] = (np.log(df["txAjuste(%)"])).round(2)
df
# %%
df["expTxAjuste"] = (np.exp(df["txAjuste(%)"])).round(2)
df
# %%
# pensar na função pra um único elemento

def fatorial(x):
    total = 1
    for i in range(2, int(x)+1):
        total *= i
    return total
# %%
#aplicando uma função aos dados
df["PrecoAjustado"].apply(fatorial)