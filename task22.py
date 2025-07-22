oquvchilar = [
    {"ism": "Ali", "baho": 4},
    {"ism": "Vali", "baho": 5},
    {"ism": "Hasan", "baho": 3},
    {"ism": "Husan", "baho": 5},
    {"ism": "Laylo", "baho": 4}
]

baho_5_soni = sum(1 for o in oquvchilar if o['baho'] == 5)
print(f"Bahosi 5 bolganlar soni: {baho_5_soni} ta")
