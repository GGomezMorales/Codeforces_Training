size = int(input())
for i in range(1, size + 1):
    list1 = [str(j) for j in range(i, 2*i)]
    list2 = list1.copy()[:-1]
    list2.reverse()
    print("".join(list1 + list2))
    