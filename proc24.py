def Even(K):
    return K % 2 == 0  
numbers = []
print("Введите 10 целых чисел:")
for i in range(10):
    num = int(input(f"Число {i+1}: "))
    numbers.append(num)
count = 0
for num in numbers:
    if Even(num):
        count += 1
print("Количество четных чисел:", count)