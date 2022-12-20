# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет



def check_number(num):
    if (num==6 or num==7):
        print("Yes")
    elif (num>0 and num<6):
        print("No")
    else:
        print("incorrect number")

day=int(input('Enter the number of the week from 1 to 7: \n'))
check_number(day)