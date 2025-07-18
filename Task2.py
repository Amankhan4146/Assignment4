# Task 2: Write and Append Data to a File

print("\n=== Task 2: Write and Append to 'output.txt' ===")

# Step 1: Take user input and write to a file
write_input = input("Enter text to write to 'output.txt': ")
with open("output.txt", "w") as file:
    file.write(write_input + "\n")

# Step 2: Append additional data
append_input = input("Enter additional text to append to the file: ")
with open("output.txt", "a") as file:
    file.write(append_input + "\n")

# Step 3: Read and display final content
print("\nFinal contents of 'output.txt':")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
