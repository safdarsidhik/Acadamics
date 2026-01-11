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

#3.
def reversDigits(n):

    s = str(n)

    s = list(s)
    s.reverse()
    s = ''.join(s)
    n = int(s)
    return n

if __name__ == "__main__":

    num = int(input("Enter a number: "))
    print(reversDigits(num))

#4.
def reverseDigits(n, revNum, basePos):
    if n > 0:
        reverseDigits(n // 10, revNum, basePos)  
        revNum[0] += (n % 10) * basePos[0]       
        basePos[0] *= 10                         

n = 4562
revNum = [0]  
basePos = [1]  
reverseDigits(n, revNum, basePos)
print(revNum[0])