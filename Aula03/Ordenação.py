# %%
import pandas as pd
pd.set_option('display.max_rows', 500)
# %%
df_produto = pd.read_csv("../Data/produto.csv")
df_produto
# %%
#ordenando por uma ou mais coluna (s) em específico
df_produto.sort_values(by=['vlPreco', 'descItem'], ascending=[False, True])
# %%
