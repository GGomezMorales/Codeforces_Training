data = input().split(" ")
k = int(data[0])
n = int(data[1])
w = int(data[2])

total_cost = int(((w * (w + 1)) / 2) * k)

if total_cost > n:
    print(total_cost - n)
else:
    print(0)
