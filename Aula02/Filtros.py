# %%

import pandas as pd
# %%
df = pd.read_csv("../Data/pedido.csv")
df
# %%
df["descUF"] == "São Paulo"
# %%
filtro_sp_ketchup = (df["descUF"] ==  "São Paulo") & (df["flKetchup"])

df[filtro_sp_ketchup]
# %%
filtro_cidades_ketchup = ((df["descUF"] ==  "São Paulo") | (df["descUF"] ==  "Rio de Janeiro") | (df["descUF"] ==  "Paraná")) & df["flKetchup"]

df[filtro_cidades_ketchup] #["flKetchup"].unique() pra confirmar que tem apenas valores unicos de determinada coluna
# %%
uf_recortes = ['São Paulo', "Rio de Janeiro", "Paraná"] 
filtro_uf_ketchup = df["descUF"].isin(uf_recortes) & df["flKetchup"]
df[filtro_uf_ketchup]
# %%
filtro_txt_na = df["txtRecado"].isna()
df[filtro_txt_na]