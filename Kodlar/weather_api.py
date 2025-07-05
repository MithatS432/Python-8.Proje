import requests

def hava_durumu(sehir):
    url = f"https://wttr.in/{sehir}?format=3"
    response = requests.get(url)
    if response.status_code == 200:
        print("Hava Durumu:", response.text)
    else:
        print("API'den veri alınamadı.")
