# 1. First, let's create a file so we have something to read
with open('sample.txt', 'w') as file:
    file.write("Hello!\nThis is line one.\nThis is line two.")

print("--- Reading the file now ---")

# 2. Now, the simple way to read it line by line
with open('sample.txt', 'r') as file:
    for line in file:
        print(line.strip()) # strip() removes the extra empty lines