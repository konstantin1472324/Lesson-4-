def min_odd_divisor(n):
    for k in range(3, int(n**0.5) + 1, 2):
        if n % k == 0:
            return k
    return n if n % 2 == 1 and n != 1 else 0
n = int(input("Введите натуральное число n: "))
result = min_odd_divisor(n)
if result == 0:
    print(f"У числа {n} нет нечетных делителей кроме 1")
else:
    print(f"Наименьший нечетный делитель числа {n} (кроме 1): {result}")