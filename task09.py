with open("Input/numbers.txt") as file:
    content = file.read()
    numbers = list(map(str, content.split()))
for i in numbers:
    print(f"{i} - {len(i)} xonali")