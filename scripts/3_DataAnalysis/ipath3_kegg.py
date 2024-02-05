import pandas as pd

eggnog = "/Users/zeyku390/PycharmProjects/Miuul/resource/eggnog/wb.csv"
out_file = "/Users/zeyku390/PycharmProjects/Miuul/data/kegg_wb.csv"


df = pd.read_csv(eggnog, header="infer", sep="\t")
# get a list of KEGG_KOs

# split the column into multiple columns
df_kegg = df.dropna(subset=["KEGG_KOs"])["KEGG_KOs"].str.split(",", expand=True)
# merge all columns into one
df_kegg_melt = pd.melt(df_kegg, value_name="KEGG_KOs").dropna(subset=["KEGG_KOs"])

# drop duplicates
df_kegg_melt = df_kegg_melt.drop_duplicates(subset=["KEGG_KOs"])
# sort
df_kegg_melt_sort = df_kegg_melt.sort_values(by=["variable"], ascending=False)
# save
df_kegg_melt_sort["KEGG_KOs"].to_csv(out_file, sep="\t", index=False, header=False)



