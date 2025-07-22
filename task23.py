oquvchilar = [
    {"ism": "Ali", "baho": 4},
    {"ism": "Vali", "baho": 5},
    {"ism": "Hasan", "baho": 3},
    {"ism": "Husan", "baho": 5},
    {"ism": "Laylo", "baho": 4}
]

baho_soni = {}

for oquvchi in oquvchilar:
    baho = oquvchi['baho']
    if baho in baho_soni:
        baho_soni[baho] += 1
    else:
        baho_soni[baho] = 1

for baho, soni in baho_soni.items():
    print(f"{baho} baho - {soni} marta")

