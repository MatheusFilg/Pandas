# %%
import pandas as pd
pd.set_option('display.max_rows', 500)
# %%
df_produto = pd.read_csv('../Data/produto.csv')
df_produto
# %%
df_produto['Categoria'] = df_produto['descItem'].apply(lambda x: x.lower().split(' ')[0])
df_produto
# %%
df_produto = df_produto.sort_values(by=['vlPreco', 'descItem'], ascending=[False, True])
#df_produto.drop_duplicates() #considera a linha inteira
df_produto.drop_duplicates(subset=['Categoria'], keep='first')#deleta deixando apenas o primeiro valor que ele encontrar da coluna
# %%
df_pedido = pd.read_csv("../data/pedido.csv")
df_pedido
# %%
#se uma linha tiver NAN toda ela morre, isso pode ser mudado com o 'how'
df_pedido.dropna(subset=['txtRecado', 'flKetchup'], how='all')
# %%
