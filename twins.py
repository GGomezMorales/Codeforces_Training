n = int(input())
values = input().split(" ")
values = list(map(int, values))
values.sort(reverse=True)
values.append(0)

for i in range(1, n + 1):
    if sum(values[0:i]) > sum(values[i:]):
        print(len(values[0:i]))
        break
