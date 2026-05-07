# File: file_operations_part2.py

FILENAME = "students.txt"

def create_and_write_file():
    """Create a file and write some lines."""
    with open(FILENAME, "w") as f:
        f.write("Alice,85\n")
        f.write("Bob,92\n")
        f.write("Charlie,78\n")
    print("File created and initial data written.")

def read_entire_file():
    """Read the whole file content."""
    with open(FILENAME, "r") as f:
        content = f.read()
    print("\n--- Entire file content ---")
    print(content)

def read_line_by_line():
    """Read file line by line."""
    print("\n--- Reading line by line ---")
    with open(FILENAME, "r") as f:
        for line in f:
            print(line.strip())

def append_to_file():
    """Append new data to the file."""
    with open(FILENAME, "a") as f:
        f.write("Diana,88\n")
        f.write("Ethan,91\n")
    print("\nNew data appended.")

def process_file():
    """
    Example processing:
    - Read all marks
    - Compute average
    - Find highest scorer
    """
    students = []
    with open(FILENAME, "r") as f:
        for line in f:
            name, mark_str = line.strip().split(",")
            students.append((name, int(mark_str)))

    total = sum(mark for _, mark in students)
    avg = total / len(students)

    top_student = max(students, key=lambda x: x[1])

    print("\n--- Processing results ---")
    print(f"Average mark: {avg:.2f}")
    print(f"Top student: {top_student[0]} with {top_student[1]}")

def main():
    create_and_write_file()
    read_entire_file()
    read_line_by_line()
    append_to_file()
    read_entire_file()
    process_file()

if __name__ == "__main__":
    main()