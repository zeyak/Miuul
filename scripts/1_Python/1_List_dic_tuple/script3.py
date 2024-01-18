'''
Bu script nükleotid sayımı yapmaktadır.
© Copyright 2024 Zeynep Akdeniz
'''

def nukleotid_sayimi(dizi):
    sayac = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    for nukleotid in dizi:
        if nukleotid in sayac:
            sayac[nukleotid] += 1
    return sayac
