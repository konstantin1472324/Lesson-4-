import math
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
def Sin1(x, epsilon):
    result = 0
    n = 0
    while True:
        term = ((-1)**n) * (x**(2*n+1)) / factorial(2*n+1)
        if abs(term) <= epsilon:
            break   
        result += term
        n += 1
    return result
x = float(input("Введите x: "))
epsilons = []
print("Введите 6 значений epsilon (ε > 0):")
for _ in range(6):
    epsilons.append(float(input()))
for eps in epsilons:
    approx = Sin1(x, eps)
    exact = math.sin(x)
    print(f"ε = {eps}: приближенное значение = {approx:.6f}, точное значение = {exact:.6f}")