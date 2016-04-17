ticket = int(input())
part1 = ticket // 1000
part2 = ticket % 1000

sumPart1 = part1 % 10 + (part1 % 100) // 10 + part1 // 100
sumPart2 = part2 % 10 + (part2 % 100) // 10 + part2 // 100


if sumPart1 == sumPart2:
    print('Счастливый')
else:
    print('Обычный')

