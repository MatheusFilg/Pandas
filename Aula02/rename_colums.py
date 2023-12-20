# %%

import pandas as pd 
# %%
df = pd.read_csv("../Data/pedido.csv")
df
# %%
df.rename(columns={"descUF":"descEstado"}) #novo df
# %%
df = df.rename(columns={"descUF":"descEstado"})#substituindo no próprio df
df #mais utilizado essa maneira devido ao encadeamento de comandos
# %%
df.rename(columns={"descUF":"descEstado"}, inplace=True) #alternativa 1
df # aqui nao existe retorno e sim apenas alterando
# %%
