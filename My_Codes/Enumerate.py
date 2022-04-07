seasons = ["Spring", "Summer", "Winter", "Cold"]

# 1st method
count = 1
for season in seasons:
    print(count, season)
    count += 1

# 2nd method
for count, season in enumerate(seasons, start=1):
    print(count, season)