def IsSquare(K):
    root = int(K ** 0.5)
    return root * root == K
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
    if IsSquare(num):
        count += 1
print("Количество квадратов чисел:", count)