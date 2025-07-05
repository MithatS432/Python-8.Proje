# Bu dosya: math_utils.py
import math
import datetime

def daire_alani(r):
    return math.pi * r ** 2

def tarih_saat():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
