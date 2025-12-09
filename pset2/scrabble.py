points = {
    "a": 1,
    "b": 3,
    "c": 3,
    "d": 2,
    "e": 1,
    "f": 4,
    "g": 2,
    "h": 4,
    "i": 1,
    "j": 8,
    "k": 5,
    "l": 1,
    "m": 3,
    "n": 1,
    "o": 1,
    "p": 3,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "v": 4,
    "w": 4,
    "x": 8,
    "y": 4,
    "z": 10,
}

word1 = input("Player 1 word: ").lower()
word2 = input("Player 2 word: ").lower()
sum1 = 0
sum2 = 0

for letter in word1:
    if letter in points:
        sum1 += points[letter]

for letter in word2:
    if letter in points:
        sum2 += points[letter]

if sum1 > sum2:
    print("Player 1 wins!")
elif sum1 < sum2:
    print("Player 2 wins!")
else:
    print("Tie!")
