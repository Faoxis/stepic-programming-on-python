x = int(input())
y = int(input())
z = int(input())

min = min(x, y, z)
max = max(x, y, z)

print(max)
print(min)

if max > x > min:
    print(x)
elif max > y > min:
    print(y)
elif max > z > min:
    print(z)
elif x == y:
    print(x)
elif y == z:
    print(z)
elif x == z:
    print(z)
