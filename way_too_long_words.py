number_words = int(input())

count = 0

while count < number_words:
    word = input()
    if len(word) <= 10:
        print(word)
    else:
        word_new = word[0] + f"{len(word) - 2}" + word[-1]
        print(word_new)
    count += 1
