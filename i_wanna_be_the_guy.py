n = int(input())
p = list(input().split(" ")[1:])
q = list(input().split(" ")[1:])
if "0" in set(q + p):
    print(["Oh, my keyboard!", "I become the guy."][n + 1 == len(set(q + p))])
else:
    print(["Oh, my keyboard!", "I become the guy."][n == len(set(q + p))])
