numbers = input()
queue = input()
time = 0

while time < int(numbers[2]):
    if "BG" in queue:
        queue = queue.replace("BG", "GB")
    time += 1

print(queue)
