import requests
from bs4 import BeautifulSoup
import pyperclip
platform = int(input("1.Trendyol\n2.Çiçek Sepeti\n3.HepsiBurada\n4.Barkod Bul\nPlatform Seçiniz: "))

if platform == 1:
    def trendyol():
        print("Trendyol")
        while True:

            satis_fiyati1 = str(input("Satış Fiyatı: "))
            alis_fiyati1 = str(input("Alış Fiyatı: "))
            komisyon_orani = float(input("Komisyon Oranı: "))

            satis_fiyati2 = satis_fiyati1.replace(",", ".")
            alis_fiyati2 = alis_fiyati1.replace(",", ".")

            satis_fiyati = float(satis_fiyati2)
            alis_fiyati = float(alis_fiyati2)

            k_o = float((satis_fiyati * komisyon_orani) / 100)

            if satis_fiyati < 20:
                kargo_ucreti1 = 3
                print("Kazancınız", satis_fiyati - alis_fiyati - k_o - kargo_ucreti1, "TL")

            elif 20 <= satis_fiyati < 30:
                kargo_ucreti2 = 4.48
                print("Kazancınız", satis_fiyati - alis_fiyati - k_o - kargo_ucreti2, "TL")

            elif 30 <= satis_fiyati < 50:
                kargo_ucreti3 = 8.26
                print("Kazancınız", satis_fiyati - alis_fiyati - k_o - kargo_ucreti3, "TL")

            elif satis_fiyati >= 50:
                kargo_ucreti4 = 11.50
                print("Kazancınız", satis_fiyati - alis_fiyati - k_o - kargo_ucreti4, "TL")


    trendyol()
    print()
elif platform == 2:
    def ciceksepeti():
        print("Çiçeksepeti")
        while True:

            satis_fiyati1 = str(input("Satış Fiyatı: "))
            alis_fiyati1 = str(input("Alış Fiyatı: "))
            komisyon_orani = float(input("Komisyon Oranı: "))

            satis_fiyati2 = satis_fiyati1.replace(",", ".")
            alis_fiyati2 = alis_fiyati1.replace(",", ".")

            satis_fiyati = float(satis_fiyati2)
            alis_fiyati = float(alis_fiyati2)

            k_o = float((satis_fiyati * komisyon_orani) / 100)

            if satis_fiyati <= 9.99:
                kargo_ucreti1 = 2
                print("Kazancınız", satis_fiyati - alis_fiyati - k_o - kargo_ucreti1, "TL")

            elif 10 <= satis_fiyati <= 19.99:
                kargo_ucreti2 = 4
                print("Kazancınız", satis_fiyati - alis_fiyati - k_o - kargo_ucreti2, "TL")

            elif 20 <= satis_fiyati <= 39.99:
                kargo_ucreti3 = 6
                print("Kazancınız", satis_fiyati - alis_fiyati - k_o - kargo_ucreti3, "TL")

            elif 40 <= satis_fiyati >= 49.99:
                kargo_ucreti4 = 8
                print("Kazancınız", satis_fiyati - alis_fiyati - k_o - kargo_ucreti4, "TL")

            elif satis_fiyati >= 50:
                kargo_ucreti5 = 10.50
                print("Kazancınız", satis_fiyati - alis_fiyati - k_o - kargo_ucreti5, "TL")


    ciceksepeti()
    print()

elif platform == 3:
    def hepsiburada():
        print("Hepsiburada")
        while True:

            satis_fiyati1 = str(input("Satış Fiyatı: "))
            alis_fiyati1 = str(input("Alış Fiyatı: "))
            komisyon_orani = float(input("Komisyon Oranı: "))

            satis_fiyati2 = satis_fiyati1.replace(",", ".")
            alis_fiyati2 = alis_fiyati1.replace(",", ".")

            satis_fiyati = float(satis_fiyati2)
            alis_fiyati = float(alis_fiyati2)

            k_o = float((satis_fiyati * komisyon_orani) / 100)

            if satis_fiyati <= 29.99:
                kargo_ucreti1 = 6
                print("Kazancınız", satis_fiyati - alis_fiyati - k_o - kargo_ucreti1, "TL")

            elif satis_fiyati >= 30:
                kargo_ucreti2 = 11.50
                print("Kazancınız", satis_fiyati - alis_fiyati - k_o - kargo_ucreti2, "TL")


    hepsiburada()
    print()
else:
    def Barkod():
        print("Barkod Bulma")


        while True:
            def convertTuple(tup):

                str = ''
                for item in tup:
                    str = str + item
                return str


            r = requests.get(input("Ürün Linki: "))
            soup = BeautifulSoup(r.text, 'html.parser')
            s = soup.find('script', type='application/javascript').string

            keyword = "barcode"
            before_keyword, keyword, after_keyword = s.partition(keyword)
            k = after_keyword
            keyword2 = ':"'
            m = before_keyword2, keyword2, after_keyword2 = k.partition(keyword2)

            str = convertTuple(m)
            keyword3 = '","'
            n = before_keyword3, keyword3, after_keyword3 = str.partition(keyword3)
            mytext = before_keyword3[3:]
            pyperclip.copy(mytext)

            print(mytext)
    Barkod()

print()
