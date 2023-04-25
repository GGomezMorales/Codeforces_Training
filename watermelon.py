w = int(input())

if w % 2 != 0 or w == 2:
    print("NO")
else:
    for i in range(2, w - 1):
        if i % 2 == 0 and (2 + i) == w:
            print("YES")
            break
