import re
f_path = "text.txt"
pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
email=[]
with open(f_path,'r') as f:
    for l in f:
        email.extend(pattern.findall(l))
print(email)
