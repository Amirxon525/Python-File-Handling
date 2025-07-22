oquvchilar = [
    {"ism": "Ali", "baho": 4},
    {"ism": "Vali", "baho": 5},
    {"ism": "Hasan", "baho": 3},
    {"ism": "Husan", "baho": 5},
    {"ism": "Laylo", "baho": 4}
]

eng_yuqori = max(oquvchilar, key=lambda o: o['baho'])
print(f"Eng yuqori baho olgan oquvchi: {eng_yuqori['ism']} ({eng_yuqori['baho']} baho)")
