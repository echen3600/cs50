c = input("Enter card number: ")

reversed_c = ""
for char in c:
    reversed_c = char + reversed_c

sum1 = 0 
sum2 = 0 

for i in range(len(reversed_c)):
    digit = int(reversed_c[i])
    
    if (i + 1) % 2 == 0:
        doubled = digit * 2
        if doubled >= 10:
            digits = str(doubled)   
            doubled = int(digits[0]) + int(digits[1])
        sum1 += doubled
    else:
        sum2 += digit

total = sum1 + sum2

if total % 10 == 0:
    print("Valid")
else:
    print("Invalid")
