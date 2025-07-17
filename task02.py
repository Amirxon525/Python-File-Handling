f1 = open('Input/students.txt')
cantent = f1.read()
f1.close()

total = sum(map(int, cantent.split()))
f2 = open("Output")