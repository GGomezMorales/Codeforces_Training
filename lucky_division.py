n = int(input())
count = 0
for i in range(1, n + 1):
    if int(str(i).count("4")) + int(str(i).count("7")) == len(str(i)):
        if n % i == 0:
            count += 1

if count >= 1:
    print("YES")
else:
    print("NO")
