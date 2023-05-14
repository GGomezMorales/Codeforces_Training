number_test = int(input())
count = 0
test = 0
while test < number_test:
    test += 1
    n = int(input())
    array = [i % 2 for i in list(map(int, input().split(" ")))]
    partern_array = [i % 2 for i in range(n)]
    if (array.count(0) != partern_array.count(0)) or (array.count(0) != partern_array.count(0)):
        print(-1)
    elif array == partern_array:
        print(0)
    else:
        for j in range(n):
            if array[j] != partern_array[j]:
                count += 1
        print(count // 2)
    array.clear()
    partern_array.clear()
    count = 0
