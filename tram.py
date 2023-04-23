tram_stops = int(input())

count_stops = 0
current_passengers = 0
list_result = []

while count_stops < tram_stops:
    exit_enter = input()
    exit_enter = exit_enter.split(" ")
    exit_passengers = int(exit_enter[0])
    enter_passengers = int(exit_enter[1])
    inside_passengers_after_start = current_passengers - exit_passengers
    current_passengers = inside_passengers_after_start + enter_passengers
    list_result.append(current_passengers)
    count_stops += 1

print(max(list_result))



