w = input().split(" ")
count = 0
a = int(w[0])
b = int(w[1])

while a <= b:
    count += 1
    a *= 3
    b *= 2

print(count)
