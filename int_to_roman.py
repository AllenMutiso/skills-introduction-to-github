
num = int(input("Enter number >>> "))
roman = str()
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

if num >= M:
    m = 'M' * (num//M)
    roman = roman + m
    num = num % M
if num < M:
    if 900 <= num < 1000:
        roman = roman + 'CM'
        num = num % (M - C)
    if 500 <= num < 900:
        roman = roman + 'D'
        num = num % D
    if 400 <= num < 500:
        roman = roman + 'CD'
        num = num % (D - C)
    if 100 <= num < 400:
        c = 'C' * (num // C)
        roman = roman + c
        num = num % C
    if 90 <= num < 100:
        roman = roman + 'XC'
        num = num % (C - X)
    if 50 <= num < 90:
        roman = roman + 'L'
        num = num % L
    if 40 <= num < 50:
        roman = roman + 'XL'
        num = num % (L - X)
    if 10 <= num < 40:
        x = 'X' * (num // X)
        roman = roman + x
        num = num % X
    if num == 9:
        roman = roman + 'IX'
        num = 0
    if 5 <= num < 9:
        roman = roman + 'V'
        num = num % V
    if num == 4:
        roman = roman + 'IV'
        num = num % (V - I)
    if 1 <= num < 4:
        i = 'I' * num
        roman = roman + i

print(roman)


    
