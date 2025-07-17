with open("Input/students.txt") as file: 
    content = file.read()
    students =  list(map(str,content.split()))
for i in students:
    print(f"{i} - {len(i)} harfdan iborat")