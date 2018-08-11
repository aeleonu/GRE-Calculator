''' Program make a simple calculator '''
import math


# This function adds two numbers 
def add(x, y):
   return x + y

# This function subtracts two numbers 
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
   return x / y

def square(x):
    return x * x

def power(x, y):
    num = 1
    for i in range(y):
        num *= x
        i = i + 1
    return num

def remainder(x, y):
    return x % y

def root(x):
    return math.sqrt(x)

def science_notation(x,y):
    num = x * 10**y
    return num

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Square")
print("6.Power")
print("7.Remainder")
print("8.Root")
print("9.Scientific Notation")


# Take input from the user 
choice = input("Enter choice(1/2/3/4/5/6/7/8/9):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))

elif choice == '5':
   print(num1,"*", num1, "=", square(num1))

elif choice == '6':
   print(num1,"**",num2,"=", power(num1,num2))

elif choice == '7':
   print(num1,"%",num2,"=", remainder(num1,num2))

elif choice == '8':
   print(num1,"**(1/2)**", "=", root(num1))

elif choice == '9':
   print(num1,"e",num2,"=", science_notation(num1,num2))
