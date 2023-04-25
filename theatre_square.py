number = input()
number = number.split(" ")

n = int(number[0])
m = int(number[1])
a = int(number[2])

area_square = n * m
area_flagstone = a ** 2

if area_square > area_flagstone:
    if n % a == 0 and m % a == 0:
        print((n // a) * (m // a))
    elif n % a == 0 and m % a != 0:
        print((n // a) * ((m // a) + 1))
    elif n % a != 0 and m % a == 0:
        print((m // a) * ((n // a) + 1))
    elif n % a != 0 and m % a != 0:
        print(((n // a) + 1) * ((m // a) + 1))
else:
    print(1)
