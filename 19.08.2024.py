#1-vazifa
class Avto:
    """Avto degan klass yaratdik"""
    def init(self,model, korobka, rang, kraska, probeg,  narh,):
        """Moshina holati"""
        self.model = model
        self.korobka = korobka
        self.rang = rang
        self.narh = narh
        self.kraska = kraska
        self.probeg = probeg

    def hususiyat(self):
        """Mashina haqida ma'lumot"""
        return f"Modeli:{self.model}, Korobkasi:{self.korobka}, Rangi:{self.rang}, Kraskasi:{self.kraska}, Yurgani {self.probeg}km, Narhi:{self.narh}$"

    def update_probeg(self):
        """Moshinaning probegiga qo'shuvchi"""
        self.probeg +=100

moshina1 = Avto('Damas','Mexanika','mokriy','toza', 50000, '8000',)
moshina1.kraska = 'orqa eshikda'

print(moshina1.hususiyat())

moshina1.update_probeg()
print(moshina1.hususiyat())


#2-Vazifa
class Avtosalon:
    """Avto salon degan yangi klass"""
    def __init__(self,salon_nomi, avtomobillar, tolov_turi, manzil):
        self.salon_nomi = salon_nomi
        self.avtomobillar = avtomobillar
        self.tolov_turi = tolov_turi
        self.manzil = manzil

    def malumot(self):
        return f"Avtosalon nomi:{self.salon_nomi}, Salondagi avtomobillar: {self.avtomobillar}, To'lov turlari: {self.tolov_turi}, Avtosalon manzili: {self.manzil}"

avtosalon = Avtosalon('Avtolayn', 'song plus chempion, dashing, tahoe, zeekr 001, malibu2', 'naqd, kridit, nasiya, lizing, barter', "Fakel do'konini yon tomoni")

print(avtosalon.malumot())
