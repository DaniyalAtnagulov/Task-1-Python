# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
def find_points():
    x1 = float(input("Enter coordinate х1: "))
    y1 = float(input("Enter coordinate y1: "))
    x2 = float(input("Enter coordinate х2: "))
    y2 = float(input("Enter coordinate y2: "))
    import math
    sqrt = round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2),2)
    print(f'Distance: (A - ({x1}, {y1}) between B - ({x2}, {y2}) = {sqrt}')
find_points()