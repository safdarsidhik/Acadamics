path = "text.txt"
lines = []
with open(path,'r') as f:
    lines=f.readlines()
lines= [l.strip() for l in lines]
print(lines)
