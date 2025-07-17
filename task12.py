with open("Input/students.txt") as file: 
    content = file.read()
    students =  list(map(str,content.split()))
print("Ismlar soni - ",len(students), " ta." )