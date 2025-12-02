# def factorial(n):
#     if n == 0 or n == 1:
#         return (1)
#     else:
#         return n*factorial(n-1)
# print(factorial(int(input("Enter the number to find the factorial : "))))


def Fibonacci(n):
    if n <= 0:
        return "Incorrect / invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
print(Fibonacci(int(input("Enter the number to find the Fibonacci series : "))))
    