savol = "Kitob nomini kiriting "
savol +="(dasturni to'xtatish uchun stop deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat == 'stop':
        break


print("Mahsulotlar buyurtma qabul qilish dasturi.")
print("Mahsulot nomini kiriting (dasturni to'xtatish uchun 'exit' deb yozing).")

mahsulotlar = []

while True: 
    mahsulot = input("Mahsulot nomi: ")
    if mahsulot == 'exit':
        break  
    mahsulotlar.append(mahsulot)

print("Buyurtma ro'yxati:")
for mahsulot in mahsulotlar:
    print(f"- {mahsulot}")


print("Muzeyga chipta narhini hisoblaydigan dastur.")

savol = "Yoshingizni kiriting (dasturni to'xtatish uchun 'exit' yoki 'quit' deb yozing): "

while True:  # abadiy tsikl
    qiymat = input(savol)
    if qiymat.lower() == 'exit' or qiymat.lower() == 'quit':
        break  # tsiklni to'xtatish
    if qiymat.isdigit():
        yosh = int(qiymat)
        if yosh < 7:
            narx = 2000
        elif 7 <= yosh < 18:
            narx = 3000
        elif 18 <= yosh < 65:
            narx = 10000
        else:
            narx = 0
        if narx == 0:
            print("Siz uchun chipta bepul.")
        else:
            print(f"Siz uchun chipta narxi: {narx} so'm.")
    else:
        print("Iltimos, to'g'ri yosh kiriting yoki dasturni to'xtatish uchun 'exit' yoki 'quit' deb yozing.")



print("E-bozor mahsulotlari va narxlari lug'atini shakllantiruvchi dastur.")
print("Mahsulot nomi va uning narhini kiriting (dasturni to'xtatish uchun 'exit' deb yozing).")

mahsulotlar_lugati = {}

while True:  
    mahsulot_nomi = input("Mahsulot nomi: ")
    if mahsulot_nomi.lower() == 'exit':
        break  
    mahsulot_narxi = input(f"{mahsulot_nomi}ning narhi: ")
    if mahsulot_narxi.lower() == 'exit':
        break  
    if mahsulot_narxi.isdigit():
        mahsulotlar_lugati[mahsulot_nomi] = int(mahsulot_narxi)
    else:
        print("Iltimos, mahsulot narhini to'g'ri kiriting.")

print("Mahsulotlar lug'ati:")
for mahsulot, narx in mahsulotlar_lugati.items():
    print(f"{mahsulot}: {narx} so'm")

