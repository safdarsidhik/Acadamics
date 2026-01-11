file = input("Enter the file name to append: ")
data = input("Enter the content: ")

try:
    with open(file, "a") as file:
        file.write(data + "\n")
    print("Successfully appended.")
except FileNotFoundError:
    print("The file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
