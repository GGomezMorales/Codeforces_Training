n = int(input())
strings = set(list(input().lower()))
print(["NO", "YES"][len(strings) == 26])
