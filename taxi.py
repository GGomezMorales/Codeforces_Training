n = int(input())
num = list(map(int, input().split()))
one_list = []
two_list = []
three_list = []
count = 0
for i in range(n):
    if num[i] == 4:
        count += 1
    elif num[i] == 3:
        three_list.append(num[i])
    elif num[i] == 2:
        two_list.append(num[i])
    elif num[i] == 1:
        one_list.append(num[i])

