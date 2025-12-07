while True:
    try:
        h = int(input('Enter height: '))
        if 1 <= h <= 8:
            break
    except ValueError:
        pass

print('')

for i in range(1, h + 1):
    print('#' * i)

print('')

for i in range(1, h + 1):
    print(' ' * (h - i) + '#' * i + ' ' + '#' * i)

