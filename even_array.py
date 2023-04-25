number_test = int(input())

iteration = 0

while iteration < number_test:
    iteration += 1
    n = int(input())
    array = input()
    array = [int(i) for i in array.split(" ")]
    i_mod_2 = [i % 2 for i in range(0, n)]
    array_mod_2 = [array[i] % 2 for i in range(0, n)]

    if i_mod_2.count(0) != array_mod_2.count(0) or i_mod_2.count(1) != array_mod_2.count(1):
        print(-1)
    elif i_mod_2 == array_mod_2:
        print(0)
    else:
        move = 0
        for i in range(0, n):
            if array_mod_2[i] != i_mod_2[i]:
                for j in range(i + 1, n):
                    if array_mod_2[j] != i_mod_2[j]:
                        array_mod_2[i], array_mod_2[j] = array_mod_2[j], array_mod_2[i]
                        move += 1
                        break
        print(move)
