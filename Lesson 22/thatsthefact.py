# to find factors of usre input

# goes frokm 1 to  number and checks is I divide the number. If yes, it isa factor
def print_factors(number):
    print("The factors of", number, "are:")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)

# Taking input from the user
number = int(input("Enter your number to find it´s factprs: "))

# Calling our functions
print_factors(number)