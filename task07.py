with open("Input/numbers.txt") as file:
    content = file.read()
    numbers = list(map(int, content.split()))
for i in numbers:
    print(pow(i,2), end=', ')