with open("Input/numbers.txt") as file:
    content = file.read()
    numbers = list(map(int, content.split()))

average_numbers = sum(numbers)
number_of_numbers = len(numbers)
print(average_numbers / number_of_numbers)