import random
import string
import enchant

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

letters = list(string.ascii_lowercase)
dictionary = enchant.Dict("en_US")


def draw_letters(player):
    while True:
        draw_list = random.sample(letters, 10)
        print(f"{player} letters: {', '.join(draw_list)}")
        choice = input("Do you want to keep these letters? (y/n): ").lower()
        if choice == "y":
            break
    while True:
        word = input(f"{player} word: ").lower()
        draw_copy = draw_list.copy()
        for letter in word:
            if letter in draw_copy:
                draw_copy.remove(letter)
            else:
                print("Word uses letters not in your draw!")
        if dictionary.check(word):
            print("Valid word!")
            break
        else:
            print("Not a valid word!")
    return word


def calc_score(word):
    return sum(points[letter] for letter in word if letter in points)


word1 = draw_letters("Player 1")
word2 = draw_letters("Player 2")

sum1 = calc_score(word1)
sum2 = calc_score(word2)

print("Player 1 points: " + str(sum1) + " vs " + "Player 2 points: " + str(sum2))

if sum1 > sum2:
    print("Player 1 wins!")
elif sum1 < sum2:
    print("Player 2 wins!")
else:
    print("Tie!")
