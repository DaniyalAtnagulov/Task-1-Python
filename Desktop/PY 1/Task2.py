# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
def true_or_false():
    for x in [0,1]: 
        for y in [0,1]:
            for z in [0,1]:                
                print(not (x or y or z)==(not x) and (not y) and (not z))
true_or_false()



