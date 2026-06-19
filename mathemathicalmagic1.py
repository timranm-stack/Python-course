def binary_to_decimal():
    # Take binary input from the user as a string
    binary_str = input("Enter your Binary: ")
    
    try:
        # The int() function with base 2 converts a binary string directly to an integer
        decimal_val = int(binary_str, 2)
        print(f"Decimal : {decimal_val}")
    except ValueError:
        # Handle cases where the user inputs characters other than 0 and 1
        print("Invalid input! Please enter a valid binary number containing only 0s and 1s.")

# Run the program
if __name__ == "__main__":
    # First example run from your image
    binary_to_decimal()
    print() # Prints a blank line for spacing
    # Second example run from your image
    binary_to_decimal()