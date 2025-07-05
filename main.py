# Bu dosya: main.py
import math_utils  # kendi oluşturduğumuz modül
import os
import sys

print("Bugünün tarihi ve saati:", math_utils.tarih_saat())

yaricap = 5
alan = math_utils.daire_alani(yaricap)
print(f"Yarıçapı {yaricap} olan dairenin alanı: {alan:.2f}")

print("Mevcut çalışma dizini:", os.getcwd())
print("Python çalıştırma yolu:", sys.executable)
