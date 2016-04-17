n = int(input())


if ((n == 1) or (n % 10 == 1) or (n % 100 == 1)) and not((11 <= n <=14) or (11 <= n % 100 <= 14)):
    print(n,'программист')
elif ((1 < n < 5) or (1 < n % 10 < 5) or (1 < n % 100 < 5)) and not((11 <= n <=14) or (11 <= n % 100 <= 14)):
    print(n, 'программиста')
else:
    print(n, 'программистов')
