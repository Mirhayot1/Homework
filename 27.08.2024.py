# 1 - Vazifa
import json
data = {
    "Model": "Malibu",
    "Rang": "Qora",
    "Yil": 2022,
    "narh": 35000
}
data_json = json.dumps(data)
print(data_json)
import json

#2 - Vazifa
talaba_json = {"ism":"Hasan","familiya":"Husanov","tyil":2000}
print(f"{talaba_json['ism']} {talaba_json['familiya']}")

#3 - vazifa
with open('data','w') as f:
    json.dump(data,f)

with open('talaba.json','w') as a:
    json.dump(talaba_json,a)
