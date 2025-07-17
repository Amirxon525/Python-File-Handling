with open("Input/students.txt") as file: 
    content = file.read()
    students =  list(map(str,content.split()))
students.sort()
print(students)