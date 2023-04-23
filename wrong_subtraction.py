numbers = input()
numbers = numbers.split(" ")

n = int(numbers[0])
k = int(numbers[1])
count = 0

while count < k:
    last_digit = n % 10
    if last_digit != 0:
        n -= 1
    else:
        n = int(n / 10)
    count += 1

print(n)

'''
last digit in another way
last_digit = int(str(n)[-1]) 

The %10 operation returns the remainder of dividing the original
number by 10, which corresponds to the last digit of the number.
'''
