#1
def yosh_hisobla():
    """Yoshingizga qarab tug'ilgan yilingizni aniqlovchi dastur"""
    ism = (input("ismingizni kiriting: "))
    yosh1 = int(input("yoshngizni kiriting: "))
    yosh2 = 2024 - yosh1
    print(f"Hurmatli {ism} siz {yosh2} - yil tug'ilgansiz")

yosh_hisobla()

#2
def hisobla():
    """sonning kvadrati va kubini aniqlovchi dastur"""
    son1 = int(input("Son kiriting: "))
    kvadrat = son1**2
    kub = son1**3
    print(f"{son1} ning kvadrati>>>> {kvadrat} ")
    print(f"{son1} ning kubi>>>>> {kub} ")


hisobla()

#3
def bir_narsa():
    """sonning juft yoki toq ekanligini aniqlovchi dastur"""
    son = int(input("Sonni kiriting: "))
    
    if son % 2 == 0:
        print(f"{son} juft son")
    else:
        print(f"{son} toq son")

bir_narsa()


#4
def sonni_top():
    """Sonning katta yoki kichikligini aniqlovchi dastur"""
    son1 = int(input("Birinchi sonni kiriting: "))
    son2 = int(input("Ikkinchi sonni kiriting: "))
    
    if son1 > son2:
        print(f"Kattasi: {son1}")
    elif son2 > son1:
        print(f"Kattasi: {son2}")
    else:
        print("Sonlar teng")

sonni_top()
