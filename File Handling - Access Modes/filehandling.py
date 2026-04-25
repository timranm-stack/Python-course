# 1. 'w' Mode (Write): Create a new file and add initial student info
# Warning: This will overwrite the file if it already exists!
with open("student_records.txt", "w") as file:
    file.write("Name: Muhammad Taha, Favorite Subject: Computer Science\n")
    print("Initial record created successfully.")

# 2. 'a' Mode (Append): Add a new student without deleting existing data
with open("student_records.txt", "a") as file:
    file.write("Name: Roy, Favorite Subject: Mathematics\n")
    print("New record appended successfully.")

# 3. 'r' Mode (Read): Open the file to see the final list
print("\n--- Current Student Records ---")
with open("student_records.txt", "r") as file:
    content = file.read()
    print(content)