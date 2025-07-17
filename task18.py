name = input ("name: ").strip ()
with open ( 'Input/students.txt') as f:
    if name in f. read().split():
        print ("mavjud.")
    else:
      print ("mavjud emas.")