file = open("Input/numbers.txt")
content = file.read()
numbers = list(map(int, content.split()))
file.close()
f = open("odd_numbers.txt", "w")
for i in numbers:
    if i % 2 == 1:
        f.write(str(i) + ", ")
f.close()