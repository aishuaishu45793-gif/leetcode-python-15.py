number = 153
digits = str(number)

total = sum(int(digit) ** len(digits) for digit in digits)

print(total == number)