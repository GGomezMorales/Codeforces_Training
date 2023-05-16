n = int(input())
i = 0
while i < n:
    numbers = list(map(int, input().split(" ")))
    a = numbers[0]
    b = numbers[1]
    if a % b != 0:
        print(b - (a % b))
    else:
        print(0)
    i += 1
