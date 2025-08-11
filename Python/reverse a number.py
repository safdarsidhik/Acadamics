#reverse a number
#1.
n = int(input("Enter a number: "))
rev = 0

while(n > 0):
    a = n % 10
    rev = rev * 10 + a
    n = n // 10

print(rev)

#2.
n = input("Enter a number: ")
rev = n[::-1]
print(rev)
