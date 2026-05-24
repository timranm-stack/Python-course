# Take input from the user
number = int(input("Input your number:"))

# calculate number of digits
digits = len(str(number))

# intialize result variable
resultNumber = 0

# find the sum of the a^digits of each digit
temp = number
while temp > 0:
    digit = temp % 10
    resultNumber += digit ** digits
    temp //= 10

# disply the result
if number == resultNumber:
    print(number,"is an Armstrong number")
else:
    print(number, "is not an armstrong number")