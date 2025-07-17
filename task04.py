file = open("Input/numbers.txt")
content = file.read()

numbers = list(map(int, content.split()))
for i in numbers:
    if i % 2 == 0:
        print(i)


file.close()



file.close()