'''
This script is used to plot the blastn results
© Copyright 2024 Zeynep Akdeniz
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


blast_G_muris = pd.read_csv('/Users/zeyku390/PycharmProjectsCE/Miuul/output/blastn/G_intestinalis/G_muris.blastn', sep='\t', header=None)
blast_S_salmonicida = pd.read_csv('/Users/zeyku390/PycharmProjectsCE/Miuul/output/blastn/G_intestinalis/S_salmonicida.blastn', sep='\t', header=None)


blast_G_muris.columns = ['qseqid', 'sseqid', 'pident', 'length', 'mismatch', 'gapopen', 'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore']
blast_S_salmonicida.columns = ['qseqid', 'sseqid', 'pident', 'length', 'mismatch', 'gapopen', 'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore']

num_hits_blast_G_muris = len(blast_G_muris)
num_hits_blast_S_salmonicida = len(blast_S_salmonicida)

print("Number of hits for Giardia intestinalis vs. Giardia muris: ", num_hits_blast_G_muris)
print("Number of hits for Giardia intestinalis vs. Spironucleus salmonicida: ", num_hits_blast_S_salmonicida)


# Create the scatter plot
plt.figure(figsize=(10,8))
sns.scatterplot(x='qseqid', y='length', data=blast_G_muris, hue='pident', palette='viridis')
sns.scatterplot(x='qseqid', y='length', data=blast_S_salmonicida, hue='pident', palette='viridis')

# Set plot title and labels
plt.title('Scatter plot of BLASTn hits')
plt.xlabel('Hit Number')
plt.ylabel('Bitscore')

# Display the plot
plt.show()