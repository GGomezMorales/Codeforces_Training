string = input()
count_lower = 0
count_upper = 0
for i in string:
    if i.islower():
        count_lower += 1
    else:
        count_upper += 1

if count_lower >= count_upper:
    print(string.lower())
else:
    print(string.upper())
