'''
Bu script pozisyon belirleme işlemi yapmaktadır.
© Copyright 2024 Zeynep Akdeniz
'''

def pozisyon_belirleme(dizi):
    pozisyon = {'A': [], 'T': [], 'G': [], 'C': []}
    for index, nukleotid in enumerate(dizi):
        if nukleotid in pozisyon:
            pozisyon[nukleotid].append(index)
    return pozisyon
