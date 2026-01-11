file = input("Enter the file name: ")

try:
    with open(file, "r") as file:
        lines = file.readlines()
    longest_line = max(lines, key=len)
    print(f"The longest line is:\n{longest_line}")
    print(f"Length: {len(longest_line.strip())} characters")
except FileNotFoundError:
    print("The file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
