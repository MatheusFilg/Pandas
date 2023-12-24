#1.Podemos remover algum tipo de massa do cardápio? 
#Qual o impacto dessa ação?

# %%
import pandas as pd
pd.set_option('display.max_rows', 500)
# %%
df_item_pedido = pd.read_csv('../data/item_pedido.csv')
df_produto = pd.read_csv('../data/produto.csv')
df_item_pedido
# %%
filtro_massa = df_item_pedido['descTipoItem'] == 'massa'
df_massa = df_item_pedido[filtro_massa].merge(df_produto, how='left')
df_massa
# %%
#usando nosso filtro pra verificar quantos pedidos únicos pra cada tipo de massa
df_group = (df_massa.groupby(by=['descItem'])['idPedido']
                    .nunique()
                    .reset_index()
)
# %%
df_group['Representação(%)'] = ((df_group['idPedido'] / df_group['idPedido'].sum()) * 100).round(2)
df_group
# %%
#Aqui estamos fazendo com que a coluna de Pedido seja contada unicamente e a de Preço somada
df_group = (df_massa.groupby(by=['descItem'])
            .agg({"idPedido":['nunique'],
                  "vlPreco":['sum']})
            .reset_index())
df_group
# %%
df_group['RepQtde(%)'] = ((df_group['idPedido'] / df_group['idPedido'].sum()) * 100).round(2)
df_group['RepReceita(%)'] = ((df_group['vlPreco'] / df_group['vlPreco'].sum()) * 100).round(2)
df_group
# %%
