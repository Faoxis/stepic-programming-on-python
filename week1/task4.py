shape = str(input())

if shape == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    print( (p * (p - a) * (p - b) * (p - c)) ** 0.5 )
elif shape == 'прямоугольник':
    a = int(input())
    b = int(input())
    print(a * b)
elif shape == 'круг':
    r = int(input())
    print( (3.14 * (r * 2) ** 2) / 4 )
