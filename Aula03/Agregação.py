# %%
import pandas as pd
pd.set_option('display.max_rows', 500)
# %%
df_produto = pd.read_csv('../data/produto.csv')
df_produto
# %%
df_produto['vlPreco'].describe()
# %%
df_produto['vlPrecoInflacao'] = (df_produto['vlPreco'] * 1.09).round(2)
df_produto.describe()
# %%
df_produto['descItemPrimeiro'] = df_produto['descItem'].apply(lambda x: x.lower().split(' ')[0])
df_produto[['descItem','descItemPrimeiro']].describe()
# %%
freq_itens = pd.value_counts(df_produto['descItemPrimeiro'])
freq_itens
# %%
df_produto.groupby(by=['descItemPrimeiro'])[['vlPreco', 'vlPrecoInflacao']].mean().round(2)
# %%
(df_produto.groupby(by=['descItemPrimeiro'])[['vlPreco', 'vlPrecoInflacao']]
            .agg('mean','min','max').round(2))