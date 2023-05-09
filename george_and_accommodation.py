n = int(input())
iteration = 0
count = 0
while iteration < n:
    iteration += 1
    pq = input().split(" ")
    p = int(pq[0])
    q = int(pq[1])
    if q - p >= 2:
        count += 1

print(count)
