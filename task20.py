oquvchilar = [
    {"ism": "Ali", "baho": 4},
    {"ism": "Vali", "baho": 5},
    {"ism": "Hasan", "baho": 3},
    {"ism": "Husan", "baho": 5},
    {"ism": "Laylo", "baho": 4}
]

jami_baho = sum(o['baho'] for o in oquvchilar)
ortalacha = jami_baho / len(oquvchilar)

print(f"Baholarning o‘rtachasi: {ortalacha:.2f}")
