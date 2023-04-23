year = input()
year = str(int(year) + 1)

while 0 < 1:
    if year.count(year[0]) > 1 or year.count(year[1]) > 1 or year.count(year[2]) > 1:
        year = str(int(year) + 1)
    else:
        year = year
        break

print(year)
