import pandas as pd
import os
# %%
CURRENT_PATH = os.path.dirname(__file__)
CONTACTS_PATH = os.path.join(CURRENT_PATH,"data","contacts.tsv")
# %%
print(CONTACTS_PATH)
contacts_df = pd.read_csv(CONTACTS_PATH, sep="\t")
print(contacts_df.head(20))
print(contacts_df.info())
print('Shape:', contacts_df.shape)
print(contacts_df['state'].describe())