standing = input()
standing = list(map(int, standing.split(" ")))

k = standing[1]

score = input()
score = list(map(int, score.split(" ")))

count = 0
for i in score:
    if i >= score[k - 1] and i != 0:
        count += 1

print(count)
