# напишіть функцію, що приймає два числа int і 
# повертає True якщо це квадрат, якщо ні - False 

print ("Робимо перевірку квадрату за двома числами")

a = 5
b = 6

def is_square(one,two):
    result = one == two
    return result

def is_kvadrat(a, b):
    nabir_1 = is_square (a,b)
    nabir_2 = is_square (b,a)
    if nabir_1 and nabir_2:
        return "is kvadrat"
    return "is not"

print(is_kvadrat(a,b))
print(is_kvadrat(2,2))

    


