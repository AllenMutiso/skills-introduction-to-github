roman_list = list ()

num = int(input('Enter a positive whole number that is less than 10,000:'))

if num >= 1000:
    thousands_place_value = (num - num % 1000)/1000
    numeral = 'M' * thousands_place_value
    roman_list.append (numeral)
if 900 <= num < 1000 or 900 <= num % 1000 < 1000:
    numeral = 'CM'
    roman_list.append (numeral)
if 900 > num >= 500 or 900 > num % 1000 >= 500:
    rem_1 = num - 500 or (num % 1000) -500
    numeral = 'D'
    roman_list.append(numeral)
if 400 <= num % 1000 < 500 or 400<= num < 500:
    numeral = 'CD'
    roman_list.append(numeral)

rem_1 = num - 500 or (num % 1000) -500
if 100 <= num % 1000 < 400 or 100 <= num < 400 or 100 <= rem_1 < 400:
    hundreds_place_value = num // 100 or num % 1000 // 100 or rem_1//100
    numeral = 'C' * hundreds_place_value
    roman_list.append (numeral)

if 90 <= num < 100 or 90 <= num % 1000 < 100 or 90 <= (num % 1000) % 100 < 100 or 90 <= rem_1 < 100:
    numeral = 'XC'
    roman_list.append (numeral)
if 50 <= num < 90 or 50 <= num % 1000 < 90 or 50 <= (num % 1000) % 100 < 90 or 50 <= rem_1 <=90:
    rem_2 = 90 - num or 90 -(num % 1000) or 90 - ((num % 1000) % 100) or 90 - rem_1
    numeral = 'L'
    roman_list.append(numeral)
if 40 <= num < 50 or 40 <= num % 1000 < 50 or 40 <= (num % 1000) % 100 < 50 or 40 <= rem_1 < 50:
    numeral = 'XL'
    roman_list.append('numeral')

rem_2 = 90 - num or 90 -(num % 1000) or 90 - ((num % 1000) % 100) or 90 - rem_1
if 10 <= num < 40 or 10 <= num % 1000 < 40 or 10 <= (num % 1000) % 100 < 40 or 10 <= rem_2 < 40:
    rem_3 = num % 10 or (num % 1000) % 10 or ((num % 1000) % 100) % 10 or rem_2 % 10
    tens_place_value = num//10 or (num % 1000)//10 or ((num % 1000)% 100) // 10 or rem_2 // 10
    numeral = 'X' * tens_place_value
    roman_list.append (numeral)

rem_3 = num % 10 or (num % 1000) % 10 or ((num % 1000) % 100) % 10 or rem_2 % 10
if num == 9 or num % 1000 == 9 or (num % 1000) % 100 == 9 or rem_1 == 9 or rem_2 == 9 or rem_3 == 9:
    numeral = 'IX'
    roman_list.append(numeral)
if 5 <= num < 9 or 5 <= num % 1000 < 9 or 5 <= (num % 1000) % 100 < 9 or 5 <= rem_1 < 9 or 5 <= rem_2 < 9 or 5 <= rem_3 < 9:
    numeral = 'V'
    roman_list.append(numeral)
    rem_4 = num - 5 or (num % 1000) - 5 or ((num % 1000) % 100) - 5 or rem_1 - 5 or rem_2 - 5 or rem_3 -5 
    if rem_4 < 4:
        ones_place_value = rem_4 / 1
        numeral = int(ones_place_value * 'I')
        roman_list.append (numeral)

elif num == 4 or (num % 1000) == 4 or ((num % 1000) % 100) == 4 or rem_1 == 4 or rem_2 == 4 or rem_3 == 4:
    numeral = 'IV'
    roman_list.append(numeral)

elif num < 4 or (num % 1000) < 4 or ((num % 1000) % 100) < 4 or rem_1 < 4 or rem_2 < 4 or rem_3 < 4:
    numeral = (num % 1000) * 'I' or ((num % 1000) % 100) * 'I' or rem_1 * 'I' or rem_2 * 'I' or rem_3 * 'I'
    roman_list.append (numeral)

print (roman_list)
print ("My name is Allen Mutiso")
