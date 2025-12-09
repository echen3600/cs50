import string

while True:
    choice = input("Encrypt or decrypt? (e/d): ")
    if choice not in ["e", "d"]:
        print('Type only "e" or "d":')
    else:
        break

if choice == "e":
    p = input("Enter plain text: ").lower()
else:
    c = input("Enter cipher text: ").lower()

k = int(input("Enter key: "))


def encrypt(p, k):
    output = ""
    for char in p:
        if char.isalpha():
            pi = ord(char) - ord("a")
            ci = (pi + k) % 26
            output += chr(ci + ord("a"))
        else:
            output += char
    return output


def decrypt(c, k):
    output = ""
    for char in c:
        if char.isalpha():
            ci = ord(char) - ord("a")
            pi = (ci - k) % 26
            output += chr(pi + ord("a"))
        else:
            output += char
    return output


if choice == "e":
    print("Cipher text:", encrypt(p, k))
else:
    print("Plain text:", decrypt(c, k))
