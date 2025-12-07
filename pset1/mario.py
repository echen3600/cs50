height = int(input('Enter height: '))
    
print('')
for i in range(1, height + 1):
    print('#' * i)

print('')
for i in range(1, height + 1):
    print(' ' * (height - i) + '#' * i + ' ' + '#' * i)