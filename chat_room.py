string = input()

for letter in string:
    if letter != "h" and letter != "e" and letter != "l" and letter != "o":
        string = string.replace(letter, "")

empty_list = []

for i in range(0, len(string)):
    if (string[i] == "h") and ("h" not in empty_list):
        empty_list.append("h")
    if (string[i] == "e") and ("e" not in empty_list) and ("h" in empty_list):
        empty_list.append("e")
    if (string[i] == "l") and ("l" not in empty_list) and ("e" in empty_list) and ("h" in empty_list):
        empty_list.append("l")
        for j in range(i + 1, len(string)):
            if (string[j] == "l") and ("l" in empty_list) and ("e" in empty_list) and ("h" in empty_list):
                empty_list.append("l")
                break
    if (string[i] == "o") and ("o" not in empty_list) and ("ll" in "".join(empty_list)) and ("e" in empty_list) and ("h" in empty_list):
        empty_list.append("o")

if "".join(empty_list) == "hello":
    print("YES")
else:
    print("NO")



