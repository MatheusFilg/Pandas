# %%

import pandas as pd
# %%

df = pd.read_csv("../Data/pedido.csv")
df
# %%
df.columns
# %%
df.shape
# %%
df.index
# %%
#deep utilizado para ter maior ctz no uso de memória
df.info(memory_usage="deep")
# %%
df.dtypes
# %%
df.head()
# %%
df.tail()
# %%
df.sample(10)
# %%

#.head() é um método/função já .head to retornando somente a função e 
#não o que ela retorna, basicamente apenas exibindo a função
