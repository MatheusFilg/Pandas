# %%
import pandas as pd
pd.set_option('display.max_rows', 500)
# %%

df_mods = pd.DataFrame(
    {
        "nome": ["Kozato0", "Sky", "Nah", "Karla"],
        "idade": [25, 34, 33, 35]
    }
)
df_mods
# %%
df_subs = pd.DataFrame(
    {
        "nome": ["Kozato0", "Sky", "Nah", "Carol", "Jonathan", "Rafael"],
        "idade": [25, 34, 33, 35, 44, 18],
        "meses_sub": [24, 1, 1, 6, 3, 8],
    }
)
df_subs
# %%
(pd.concat([df_mods, df_subs])
    .sort_values(['nome', 'meses_sub'])
    .drop_duplicates(subset=['nome'])
    .fillna(0)
)