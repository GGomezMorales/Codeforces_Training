n = int(input())

count = 0
iteration = 0
while iteration < n:
    iteration += 1
    team = input()
    team = team.split(" ")
    if team.count("1") >= 2:
        count += 1

print(count)
