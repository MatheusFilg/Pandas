# %%
import pandas as pd
pd.set_option('display.max_rows', 500)
# %%
df_item_pedido = pd.read_csv('../data/item_pedido.csv')
df_pedido = pd.read_csv('../data/pedido.csv')
df_item_pedido.head(30)
# %%
df_produto = pd.read_csv('../data/produto.csv')
df_produto
# %%
#partindo de onde quero "colocar" a informação desejada
df_join = df_item_pedido.merge(right=df_produto, how='left', on=['descItem'])
df_join.merge(df_pedido, how='left')
# %%
#Maneira diferente de fazer a célula acima
df_join = (df_item_pedido.merge(right=df_produto, how='left', on=['descItem'])
                         .merge(df_pedido,how='left'))
df_join
# %%
