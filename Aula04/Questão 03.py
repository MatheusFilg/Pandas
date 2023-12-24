# Vários queijos estão estragando pela validade.
# Quais queijos juntos atendem 90% dos pedidos?

# %%
import pandas as pd
pd.set_option('display.max_rows', 500)
# %%
df_item_pedido = pd.read_csv('../data/item_pedido.csv')
df_item_pedido
# %%
filtro_queijo = df_item_pedido['descTipoItem'].isin(['queijo 1', 'queijo 2'])
df_queijo = df_item_pedido[filtro_queijo]
# %%
df_group = (df_queijo.groupby(['descItem'])['idPedido']
                     .nunique()
                     .reset_index()
                     .sort_values('idPedido', ascending=False)
                     )
df_group
# %%
df_group['Representação(%)'] = ((df_group['idPedido'] / df_group['idPedido'].sum()) * 100).round(2)
df_group['%Acum'] = df_group['Representação(%)'].cumsum()
df_group