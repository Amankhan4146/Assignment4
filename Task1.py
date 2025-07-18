# Task 1: Read a File and Handle Errors

print("=== Task 1: Reading from 'sample.txt' ===")
try:
    with open("sample.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")


