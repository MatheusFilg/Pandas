# %%

import pandas as pd
# %%
idades = [32,56,44,27,11,24,99,88,63]

s_idades = pd.Series(idades)
s_idades
# %%
media = s_idades.mean()
media
# %%
variancia = s_idades.var()
variancia
# %%
desv_pad = s_idades.std()
desv_pad
# %%
geral = s_idades.describe()
geral
# %%
#Retornando apenas valores maiores que 30
filtro = s_idades >= 30
s_idades[filtro]
# %%
#Retornando apenas valores menores que 30
s_idades[~filtro]