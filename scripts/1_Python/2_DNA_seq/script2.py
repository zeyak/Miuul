'''
Bu script tandem repeat işlemi yapmaktadır.
© Copyright 2024 Zeynep Akdeniz
'''

#Verilen dizi 5 tane tandem repeat şekline sokulur.
def tandem_repeat(dizi, tekrar_sayisi=5):
    return dizi * tekrar_sayisi

dna_dizisi = "AGCTATAG"
tandem_dna_dizisi = tandem_repeat(dna_dizisi)