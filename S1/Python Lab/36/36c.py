file = input("Enter the file name: ")

try:
    
    with open(file, "r") as file:
        lines = file.readlines()
    
    print("Actual Content of the File:")
    print("".join(lines))  

    non_comment_lines = [line for line in lines if not line.strip().startswith("#")]

    print("\nFile Content Without Comments:")
    print("".join(non_comment_lines))  
except FileNotFoundError:
    print("The file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
