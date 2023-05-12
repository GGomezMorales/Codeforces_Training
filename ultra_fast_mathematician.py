number1 = input()
number2 = input()
result = ""
for i in range(len(number1)):
    if number1[i] == number2[i]:
        result += "0"
    else:
        result += "1"

print(result)
