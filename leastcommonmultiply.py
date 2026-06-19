import math

def find_lcm():
    # Take user inputs exactly as formatted in the assignment image
    try:
        num1 = int(input("Enter Largest number : "))
        num2 = int(input("Enter Smallest number : "))
        
        # Calculate LCM using the standard mathematical formula: (a * b) // GCD(a, b)
        # Python's built-in math.gcd finds the Greatest Common Divisor
        lcm_val = abs(num1 * num2) // math.gcd(num1, num2)
        
        print(f"LCM is : {lcm_val}")
        
    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    find_lcm()