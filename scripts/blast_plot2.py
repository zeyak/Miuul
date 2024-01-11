import pandas as pd
import seaborn as sns

blast_G_muris = pd.read_csv('/Users/zeyku390/PycharmProjectsCE/Miuul/output/blastn/G_intestinalis/G_muris.blastn',
                            sep='\t', header=None)

blast_G_muris.columns = ['qseqid', 'sseqid', 'pident', 'length', 'mismatch', 'gapopen', 'qstart',
                         'qend', 'sstart', 'send', 'evalue', 'bitscore']

sns.histplot(data=blast_G_muris, x='pident')

#sns.scatterplot(data=blast_G_muris.reset_index(), x='index', y='bitscore', hue='pident')

#sns.scatterplot(data=blast_G_muris.reset_index(), x='index', y='length', hue='pident')

#pivot_table = pd.pivot_table(blast_G_muris, values='length', index='qseqid', columns='sseqid')
#sns.heatmap(pivot_table)
