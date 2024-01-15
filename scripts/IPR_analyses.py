'''
This script is used to analyse the IPR annotations of the G. muris genes
© Copyright 2024 Zeynep Akdeniz
'''

import pandas as pd
import matplotlib.pyplot as plt

# read csv
df = pd.read_csv("/Users/zeyku390/PycharmProjects/Miuul/resource/interproscan/G_muris.tsv", sep="\t",
                 names=list(range(0, 15)),
                 engine='python', quoting=3)[[0, 3, 4, 5, 11, 12]]

#get IPR annotation from column 11 for each gene
df_ipr = df[[0, 11]]
df_ipr = df_ipr.dropna().drop_duplicates().rename(columns={0: "id", 11: "ipr"})


# plot the most common IPRs
df_ipr["ipr"].value_counts()[:10].plot(kind="bar")
plt.show()

