def triangle_area(x1, y1, x2, y2, x3, y3):
    area = 0.5 * abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))
    return area
print("Введите координаты первого треугольника (x1 y1 x2 y2 x3 y3):")
x1, y1, x2, y2, x3, y3 = map(float, input().split())
area1 = triangle_area(x1, y1, x2, y2, x3, y3)
print("Введите координаты второго треугольника (x1 y1 x2 y2 x3 y3):")
x4, y4, x5, y5, x6, y6 = map(float, input().split())
area2 = triangle_area(x4, y4, x5, y5, x6, y6)
if area1 > area2:
    print("Первый треугольник имеет большую площадь")
elif area2 > area1:
    print("Второй треугольник имеет большую площадь")
else:
    print("Треугольники имеют равную площадь")