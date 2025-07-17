with open("Input/numbers.txt") as file:
    content = file.read()
    numbers = list(map(int, content.split()))
    print(numbers)
    numbers.sort()

with open("sorted_numbers.txt", 'w') as sorted_file:
    sorted_file.writelines(list(map(lambda x: str(x) + ', ',numbers)))