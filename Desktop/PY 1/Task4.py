# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


def show_range(num):
    if   num == 1: print(" The first axis: x from 0 to + ∞, y from 0 to + ∞") 
    elif num == 2: print(" The second axis: x from 0 to  - ∞, y from 0  to + ∞ ")  
    elif num == 3: print(" The third axis: x from 0 to  - ∞, y from 0  to - ∞ ")
    elif num == 4: print(" The four axis: x from 0 to  + ∞, y from 0  to - ∞ ")
    else: print("Incorrect number") 

quarter = int (input("Enter the number of quarter from 1 to 4: "))
show_range(quarter)