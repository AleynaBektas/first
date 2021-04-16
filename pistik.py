import random
from os import system


class iskambil():
    def __init__(self, dosya_adı, birinci_kul, ikinci_kul):
        self.dosya_adı = dosya_adı
        self.birinci_kul = birinci_kul
        self.ikinci_kul = ikinci_kul
        self.calisma = True

    def deste_böl(self):
        with open(self.dosya_adı, "r", encoding="utf-8") as file:
            kart_listesi = file.readlines()
            random.shuffle(kart_listesi)  # kartları karıştır
            print(kart_listesi)
            self.kullanıcı1_numaraları = []
            self.kullanıcı2_numaraları = []
            self.kullanıcı1_kart = kart_listesi[:26]
            for i in self.kullanıcı1_kart:
                self.kullanıcı1_numaraları.append(i.split(" ")[1].strip("\n"))
            self.kullanıcı2_kart = kart_listesi[26:]
            for i in self.kullanıcı2_kart:
                self.kullanıcı2_numaraları.append(i.split(" ")[1].strip("\n"))
            print(self.kullanıcı1_numaraları)
            print(self.kullanıcı2_numaraları)

    def start(self):
        print("oyun başlıyor ")
        self.masadaki_kartlar = []
        self.kullanıcı1_alınan = []
        self.kullanıcı2_alınan = []
        self.i = 0
        self.j = 0
        self.sıra = 0
        while (self.sıra < 52):
            self.puan_hesapla()
            self.baslat()


    def baslat(self):
        if (self.sıra % 2 != 0):
            print("oyun sırası {}'da".format(self.birinci_kul))
        else:
            print("oyun sırası {}'da".format(self.ikinci_kul))
        basla = input("kart atmak için e'ye basınız:")
        if (basla == "e"):
            if (self.sıra % 2 != 0):
                # kullanıcı1 tekse kullanıcı2 çiftse
                self.masadaki_kartlar.append(self.kullanıcı1_kart[self.j])
                self.j += 1
            else:
                self.masadaki_kartlar.append(self.kullanıcı2_kart[self.i])
                self.i += 1
            print("atılan kart", self.masadaki_kartlar[-1])

            if (len(self.masadaki_kartlar) >= 2 and self.masadaki_kartlar[-2].split(" ")[1] ==
                    self.masadaki_kartlar[-1].split(" ")[1]):
                for kart in self.masadaki_kartlar:
                    if (self.sıra % 2 != 0):
                        self.kullanıcı1_alınan.append(kart)
                    else:
                        self.kullanıcı2_alınan.append(kart)
                self.masadaki_kartlar = []
            print(self.masadaki_kartlar)
            self.sıra += 1


    def puan_hesapla(self):
        print("puan:")
        print("\t {}: {}\t {}: {}".format(self.birinci_kul, len(self.kullanıcı1_alınan), self.ikinci_kul,
                                          len(self.kullanıcı2_alınan)))


oyun = iskambil("iskambilKartları.txt", "aleyna", "rıdvan")
oyun.deste_böl()
oyun.start()