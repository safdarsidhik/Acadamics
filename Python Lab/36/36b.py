import re

file = input("Enter the file name: ")

try:
    with open(file, "r") as file:
        content = file.read()
    ph_numbers = re.findall(r"\b\d{10}\b", content)  
    print("Extracted Phone Numbers:")
    for number in ph_numbers:
        print(number)
except FileNotFoundError:
    print("The file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
