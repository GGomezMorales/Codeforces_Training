s = input()
t = input()

s = [i for i in s]
s.reverse()

if "".join(s) == t:
    print("YES")
else:
    print("NO")
