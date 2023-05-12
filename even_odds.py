numbers = list(map(int, input().split(" ")))
n = numbers[0]
k = numbers[1]

if n % 2 == 0 and k > n // 2:
    print(2 * k - n)
elif n % 2 == 0 and k <= n // 2:
    print(2 * k - 1)
elif n % 2 != 0 and k > (n // 2) + 1:
    print(2 * k - n - 1)
elif n % 2 != 0 and k <= (n // 2) + 1:
    print(2 * k - 1)
