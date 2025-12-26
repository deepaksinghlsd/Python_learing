#function: This module contains utility function for mathematical operations .
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
# def add(a , b) :
#     return a+b

# print(add(a,b))

add = lambda a,b : a + b 
print(f"addition of two numebr  from lambda function : {add(a,b)}")

# lambda functiions are used for small operations where we dont want to define a full function using def keyword .

#  Recursion : A function calling itself is called recursion .

def factorial (n) :
    if n == 0 or n == 1 :
        return 1 
    else : 
        return n * factorial(n-1)
    
    
num = int(input("Enter a number to find factorial : "))

print(f"Factorial of {num} is {factorial(num)}")

def print_name_age(name , age) :
    print(f"Hello {name} your age is {age} , You are {age} years oled .")

name = str(input("Enter your name :"))
age = int (input("Enter your age : "))

print_name_age(name , age)
