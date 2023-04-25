n = int(input())

x = 0
iteration = 0

while iteration < n:
    sentence = input()
    if "++" in sentence:
        x += 1
    elif "--" in sentence:
        x -= 1
    iteration += 1

print(x)
