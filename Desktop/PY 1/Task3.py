# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:


def quarter_axis(a,b):
  
    if (a>0 and b>0):
        print("First quarter")
    elif (a<0 and b>0):
        print('Second quarter')
    elif (a<0 and b<0):
        print ("Third quater")
    elif (a>0 and b<0):
        print ("Fourth quarter")

x=int(input("Enter X: \n"))
y=int(input("Enter Y: \n"))

quarter_axis(x,y)
            
