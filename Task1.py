# Task 1: Read a File and Handle Errors with Line Numbers

print("=== Task 1: Reading from 'sample.txt' ===")
try:
    with open("sample.txt", "r") as file:
        for idx, line in enumerate(file, start=1):
            print(f"Line {idx}: {line.strip()}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
