import matplotlib.pyplot as plt
from collections import Counter
import re

def dosya_oku(dosya_yolu):
    with open(dosya_yolu, 'r', encoding='utf-8') as dosya:
        return dosya.read()

def metni_temizle(metin):
    metin = metin.lower()
    metin = re.sub(r'\W+', ' ', metin)
    return metin

def kelime_frekansini_grafikle(kelime_sayilari):
    kelimeler, sayilar = zip(*kelime_sayilari.most_common(10))
    plt.bar(kelimeler, sayilar)
    plt.xlabel('Kelimeler')
    plt.ylabel('Frekans')
    plt.title('En Sık Kullanılan 10 Kelime')
    plt.show()

def ana():
    dosya_yolu = 'sample.txt'  # Kendi dosya yolunuzla değiştirin
    metin = dosya_oku(dosya_yolu)
    temizlenmis_metin = metni_temizle(metin)
    kelime_sayilari = Counter(temizlenmis_metin.split())
    kelime_frekansini_grafikle(kelime_sayilari)

if __name__ == "__main__":
    ana()