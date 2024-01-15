'''
This is a script to run tRNAscan-SE
© Copyright 2024 Zeynep Akdeniz
'''

from snakemake.shell import shell

genome = snakemake.input.genome
tRNA = snakemake.output.tRNA
stats = snakemake.output.stats

shell(f"""tRNAscan-SE {genome} -o {tRNA} -m {stats}""")