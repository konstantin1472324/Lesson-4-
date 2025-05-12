def IsPower5(K):
    if K == 1:
        return True   
    power = 5
    while power <= K:
        if power == K:
            return True
        power *= 5
    return False
numbers = []
print("Введите 10 целых положительных чисел:")
for i in range(10):
    num = int(input(f"Число {i+1}: "))
    while num <= 0:
        print("Число должно быть положительным!")
        num = int(input(f"Число {i+1}: "))
    numbers.append(num)
count = 0
for num in numbers:
    if IsPower5(num):
        count += 1
print("Количество степеней числа 5:", count)