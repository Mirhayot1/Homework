def kopaytma(*sonlar):
    """Kiritilgan sonlar ko'paytmasini hisoblaydigan funksiya"""
    if not sonlar:
        return 1
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    return kopaytma

print(kopaytma(5, 44))

def talaba_malumotlar(isim, familiya, **qolgan_malumotlar):

    """Talabalar haqida ma'lumot oluvchi funksiya"""

    malumotlar = {
        'isim': isim,
        'familiya': familiya
    }


    malumotlar.update(qolgan_malumotlar)

    return malumotlar

print(talaba_malumotlar('kimdir', 'polankasov', yosh=25, fakultet='nimadir', kurs=1))
