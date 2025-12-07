dollars = float(input("Change owed: "))
cents = dollars * 100
coins = 0

for coin in [25, 10, 5, 1]:
    coins += cents // coin
    cents = cents % coin

print(int(coins))

