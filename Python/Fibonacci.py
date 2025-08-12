#generate the Fibonacci series up to the nth term
#1.
n = int(input("Enter the number of terms: "))

a, b = 0, 1

print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#2.
n = int(input("Enter number of terms: "))
fib = [0, 1]

for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])

print("Fibonacci series:", fib[:n])

