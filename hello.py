# def factorial(n):
#     if n == 0 or n == 1:
#         return (1)
#     else:
#         return n*factorial(n-1)
# print(factorial(int(input("Enter the number to find the factorial : "))))


# def Fibonacci(n):
#     if n <= 0:
#         return "Incorrect / invalid input"
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)
# print(Fibonacci(int(input("Enter the number to find the Fibonacci series : "))))

class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def info(self):
        print(f"{self.name} is {self.age}years old")
class employee(person):
    def __init__(self,name,age,language,job):
        super().__init__(name,age)
        self.language=language
        self.job=job
    def info(self):
        super().info()
        print(f"{self.name} knows {self.language} and works as a {self.job}")   
        
a=employee(input("enter name : "),int(input("enter ur age : ")),input("enter your language : "),input("enter your job : "))
a.info()




