n = int(input())
ref_pole = input()
count = 1
for i in range(n-1):
    pole = input()
    if pole != ref_pole:
        ref_pole = pole
        count += 1

print(count)
