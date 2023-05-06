username = list(input())
nickname = username.copy()
count = len(username)

for i in username:
    letter_count = nickname.count(i)
    if letter_count > 1:
        nickname.remove(i)
        count -= 1

if count % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
