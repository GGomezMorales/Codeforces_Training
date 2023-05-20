n = int(input())
a = list(map(int, input().split(" ")))
lengt_list = []
aux_list = []
for i in range(n - 1):
    if a[i] <= a[i + 1]:
        aux_list.append(a[i])
    else:
        lengt_list.append(len(aux_list) + 1)
        aux_list.clear()

print(max(lengt_list))


