def Calc(A, B, Op):
    if Op == 1:
        return A - B    
    elif Op == 2:
        return A * B   
    elif Op == 3:
        return A / B    
    else:
        return A + B   
A = float(input("Введите число A: "))
B = float(input("Введите число B: "))
N1 = int(input("Введите операцию N1 (1-выч, 2-умн, 3-дел, иное-слож): "))
N2 = int(input("Введите операцию N2: "))
N3 = int(input("Введите операцию N3: "))
print("Результат 1:", Calc(A, B, N1))
print("Результат 2:", Calc(A, B, N2))
print("Результат 3:", Calc(A, B, N3))