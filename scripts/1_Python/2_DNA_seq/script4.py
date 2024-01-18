'''
Bu script DNA dizisini RNA dizisine çevirmektedir.
© Copyright 2024 Zeynep Akdeniz
'''

#Verilen diziyi RNA dizisine çevirir.
def rna_cevir(dizi):
    return dizi.replace("T","U")

dna_dizisi = "AGCTATAG"
rna_dizisi = rna_cevir(dna_dizisi)




