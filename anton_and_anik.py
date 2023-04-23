number_games_played = input()
result = input()

if result.count("A") > result.count("D"):
    print("Anton")
elif result.count("A") < result.count("D"):
    print("Danik")
else:
    print("Friendship")
  