n = int(input())
expression = ""
sentences = ["I hate that I love that ", "that ", "it"]
if n == 1:
    print("I hate it")
elif n % 2 == 0:
    expression = (n // 2) * "I hate that I love that "
    expression = expression[:-5] + "it"
    print(expression)
elif n % 2 != 0:
    expression = "I hate that " + (n // 2) * "I love that I hate that "
    expression = expression[:-5] + "it"
    print(expression)
