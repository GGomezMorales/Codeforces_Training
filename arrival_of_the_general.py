n = int(input())
soldiers = list(map(int, input().split()))
count_moves_max = 0
count_moves_min = 0
loop = True
while loop:
    if soldiers[0] != max(soldiers):
        i = soldiers.index(max(soldiers))
        soldiers[i], soldiers[i - 1] = soldiers[i - 1], soldiers[i]
        count_moves_max += 1
    elif soldiers[-1] != min(soldiers):
        soldiers.reverse()
        i = soldiers.index(min(soldiers))
        soldiers[i], soldiers[i - 1] = soldiers[i - 1], soldiers[i]
        count_moves_min += 1
        soldiers.reverse()
    else:
        loop = False

print(count_moves_max + count_moves_min)