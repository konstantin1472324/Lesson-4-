def Quarter(x, y):
    if x > 0 and y > 0:
        return 1    
    elif x < 0 and y > 0:
        return 2    
    elif x < 0 and y < 0:
        return 3    
    else:
        return 4    
for i in range(1, 4):
    x = float(input(f"Введите x координату {i}-й точки: "))
    y = float(input(f"Введите y координату {i}-й точки: "))
    print(f"Точка находится в {Quarter(x, y)}-й четверти")