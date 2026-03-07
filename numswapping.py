# Number swapping program

# Given numbers
x = 5
y = 9
z = 1

print("Original values:")
print("x =", x, "y =", y, "z =", z)

# Put the numbers into a list
nums = [x, y, z]

# Sort the list in ascending order
nums.sort()

# Assign back to x, y, z
x, y, z = nums

print("\nValues after swapping into ascending order:")
print("x =", x, "y =", y, "z =", z)
