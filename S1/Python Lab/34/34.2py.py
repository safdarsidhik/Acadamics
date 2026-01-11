import re

def extract_words(filename):
    pattern = re.compile(r'\b[aeiouAEIOU][a-zA-Z]*[aeiouAEIOU]\b')  
    with open(filename, 'r') as file:
        content = file.read()
        words = pattern.findall(content)
    return words


input_file = 'sample.txt'  
words = extract_words(input_file)
print("Words starting and ending with a vowel:", words)
