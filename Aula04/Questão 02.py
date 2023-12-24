# 2.Podemos deixar a de Catupiry como borda padrão?
# %%
import pandas as pd
pd.set_option('display.max_rows', 500)
# %%

df_item_pedido = pd.read_csv('../data/item_pedido.csv')
df_item_pedido
# %%
filtro_borda = df_item_pedido['descTipoItem'] == 'borda'
df_borda = df_item_pedido[filtro_borda]
df_borda
# %%
df_group = (df_borda.groupby(['descItem'])['idPedido']
         .nunique()
         .reset_index()
)
df_group
# %%
df_group['Representação(%)'] = ((df_group['idPedido'] / df_group['idPedido'].sum()) * 100).round(2)
df_group
# %%
