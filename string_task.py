string = input()
empty_list = []
vowels = ["a", "A", "e", "E", "y", "Y", "i", "I", "o", "O", "u", "U"]
for vowel in vowels:
    string = string.replace(vowel, "")
for i in string.lower():
    empty_list.append(".")
    empty_list.append(i)

print("".join(empty_list))
