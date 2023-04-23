numbers = input()
h_friends = input()
h_friends = h_friends.split(" ")
width = 0

for h in h_friends:
    if int(h) > int(numbers[2]):
        width += 2
    else:
        width += 1

print(width)