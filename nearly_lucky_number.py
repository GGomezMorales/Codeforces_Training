nearly_lucky_number = input()

lucky_number = str(
    int(nearly_lucky_number.count("7")) +
    int(nearly_lucky_number.count("4"))
)

count_digit = 0
for i in lucky_number:
    if i == "7" or i == "4":
        count_digit += 1
    else:
        count_digit = 0

if count_digit == len(lucky_number):
    print("YES")
else:
    print("NO")