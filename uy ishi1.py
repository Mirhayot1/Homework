mualliflar_asarlari = {
    "Abu Abdulloh Muhammad ibn Ismoil": [
        "Al-jome’ as-sahih",
        "Al-adab al-mufrad",
        "At-tarix al-kabir",
        "At-tarix as-sag‘ir"
    ],
    "Abdulla Qodiriy": [
        "O’tkan kunlar",
        "Mehrobdan Chayon",
        "Obid ketmon"
    ],
    "Erkin Vohidov": [
        "Tong nafasi",
        "Qo‘shiqlarim sizga",
        "O‘zbegim",
        "Qiziquvchan Matmusa"
    ],
    "Alisher Navoiy": [
        "Xamsa",
        "Lison ut-Tayr",
        "Mahbub Al-Qulub",
        "Munojot"
    ]
}

for muallif, asarlar in mualliflar_asarlari.items():
    print(f"{muallif} ning mashhur asarlari:")
    for asar in asarlar:
        print(f"- {asar}")
    print()




mashhur_shaxslar = [
    {
        "ismi": "Abu Abdulloh Muhammad ibn Ismoil",
        "tugilgan_yili": 810,
        "tugilgan_joyi": "Buxoro",
        "umr_yili": 60
    },
    {
        "ismi": "Abdulla Qodiriy",
        "tugilgan_yili": 1894,
        "tugilgan_joyi": "Toshkent",
        "umr_yili": 44
    },
    {
        "ismi": "Erkin Vohidov",
        "tugilgan_yili": 1936,
        "tugilgan_joyi": "Farg'ona",
        "umr_yili": 80
    },
    {
        "ismi": "Alisher Navoiy",
        "tugilgan_yili": 1441,
        "tugilgan_joyi": "Xirot",
        "umr_yili": 60
    }
]

for shaxs in mashhur_shaxslar:
    print(f"Ismi: {shaxs['ismi']}")
    print(f"Umr yili: {shaxs['umr_yili']}")
    print(f"Tugilgan joyi: {shaxs['tugilgan_joyi']}")
    print(f"Umr yili: {shaxs['umr_yili']}")
    print()



dostlar_kinolari = {
    "Ali": [
        "Terminator",
        "Rambo",
        "Titanic"
    ],
    "Vali": [
        "Tenet",
        "Inception",
        "Interstellar"
    ],
    "Hassan": [
        "Abdullajon",
        "Bomba",
        "Shaytanat"
    ],
    "Husan": [
        "Mahallada duv-duv gap",
        "John Wick"
    ]
}

for dost, kinolar in dostlar_kinolari.items():
    print(f"{dost} ning sevimli kinolari:")
    for kino in kinolar:
        print(f" - {kino}")
    print()  # Bo'sh satr ajratish uchun


davlatlar = {
    "O'zbekiston": {
        "poytaxti": "Toshkent",
        "hududi": "448978 kv.km",
        "aholisi": 33000000,
        "pul_birligi": "so'm"
    },
    "Rossiya": {
        "poytaxti": "Moskva",
        "hududi": "17098246 kv.km",
        "aholisi": 144000000,
        "pul_birligi": "rubl"
    },
    "AQSH": {
        "poytaxti": "Vashington",
        "hududi": "9631418 kv.km",
        "aholisi": 327000000,
        "pul_birligi": "dollar"
    },
    "Malayziya": {
        "poytaxti": "Kuala-Lumpur",
        "hududi": "329750 kv.km",
        "aholisi": 25000000,
        "pul_birligi": "rinngit"
    }
}

for davlat, malumot in davlatlar.items():
    print(f"Davlat: {davlat}")
    print(f"  Poytaxti: {malumot['poytaxti']}")
    print(f"  Hududi: {malumot['hududi']}")
    print(f"  Aholisi: {malumot['aholisi']}")
    print(f"  Pul birligi: {malumot['pul_birligi']}")
    print()
