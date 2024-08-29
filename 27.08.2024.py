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
import json

talaba = 'students.json'

with open(talaba, 'r') as file:
    data = json.load(file)

students = data['student']


for student in students:
    name = student["name"]
    lastname = student["lastname"]
    year = student["year"]
    faculty = student["faculty"]
    print(f"{name} {lastname}, {year}-kurs, {faculty} talabasi")

