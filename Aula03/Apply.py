# %% 
import pandas as pd
# %%
df_produto = pd.read_csv("../Data/produto.csv")
df_produto
# %%
df_produto['descItem'].unique()
# %%
def is_massa(x):
    return x.lower().startswith('massa')

#usando apply pra trazer nossa função aplicando no df
filtro_massa = df_produto['descItem'].apply(is_massa)
df_produto[filtro_massa]
# %%
#usando lambda pra criar uma função anônima que só sera utilizada aqui
filtro_massa = df_produto['descItem'].apply(lambda x: x.lower().startswith('massa'))
df_produto[filtro_massa]
# %%
# terceira maneira geralmente mais utilizada quando só estamos tratando do msm tipo
filtro_massa = df_produto['descItem'].str.lower().str.startswith('massa')
df_produto[filtro_massa]
# %%
