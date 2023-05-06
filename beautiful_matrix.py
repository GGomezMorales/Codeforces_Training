row1 = input(); row1 = row1.split(" ")
row2 = input(); row2 = row2.split(" ")
row3 = input(); row3 = row3.split(" ")
row4 = input(); row4 = row4.split(" ")
row5 = input(); row5 = row5.split(" ")

matrix = [row1, row2, row3, row4, row5]

for i in range(0, 5):
    for j in range(0, 5):
        if matrix[i][j] == "1":
            print(abs(2 - i) + abs(2 - j))
            break
