''' Program make an abstract calculator '''
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

# Takes the square of a number
def square(x):
    return x * x

# Gets a number to a certain power
def power(x, y):
    num = 1
    for i in range(y):
        num *= x
        i = i + 1
    return num

# Gets the remaining value
def remainder(x, y):
    return x % y

# Gets the square root of a number
def root(x):
    return x ** (0.5)

# Get the number in Scientific Notation
def science_notation(x,y):
    num = x * 10**y
    return num

## AREA FORMULAS ##
#Area of A Square
def squarea(x):
    return square(x)

#Area of a Rectangle
def rectarea(x, y):
    return multiply(x, y)

#Area of a triangle with 2 sides
def triarea(x, y):
    return 0.5 * multiply(x, y)

#Area of triangle with all 3 sides
def side_triarea(a, b, c):
    N = (a + b + c)/2
    num = (N - a)*(N - b)*(N - c)
    value = N*num
    return root(value)

#Area of a trapezoid
def trapezarea(x, y, z):
   n = (x + y)/2
   return multiply(n, z)

#Area of Circle
def cirlerea(x):
   return math.pi * square(x)

##CIRCUMFERENCE##
def circumrad(x):
   return math.pi * (x**2)

def circumdi(x):
   return math.pi * x

##TRIGNOMETRY##:
def sine_for_sides(x,y,z):
   a = y/math.sin(y)
   value = a * math.sin(x)
   return value

def cos_for_sides(x,y,z):
   num = (y**2) + (z**2) - (2*y*z)*math.cos(x)
   return num

def sine_for_angles(x,y):
   a = math.sin(y)/y
   b = a * x
   num = math.asin(b)
   return num * 100

def cos_for_angles(x,y,z):
   num = (y**2) + (z**2) - (x**2)
   return (num / (2 * y * z)) * 100


## CALCULATOR ##
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
print("10.Area")
print("11.Trignometry")

# Take input from the user 
choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11):")
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

elif choice == '10':
    print("1.Square")
    print("2.Rectangle")
    print("3.Triangle")
    print("4.Sides of Triangle")
    print("5.Trapezoid")
    print("6.Circle")
    area_choices = input("Enter choice(1/2/3/4/5/6):")
    if area_choices == '1':
        print(squarea(num1))
    elif area_choices == "2":
        print(rectarea(num1, num2))
    elif area_choices == "3":
        print(triarea(num1, num2))
    elif area_choices == "4":
        num3 = int(input("Enter third number: "))
        print(side_triarea(num1, num2, num3))
    elif area_choices == "5":
        num3 = int(input("Enter third number: "))
        print(trapezarea(num1, num2, num3))
    elif area_choices == "6":
        print(cirlerea(num1))

elif choice == '11':
   print("1. Find Sides")
   print("2. Find Angles")
   num3 = int(input("Enter third number: "))
   options = input("Enter choice(1/2):")
   if options == '1':
      print("1.Sine")
      print("2.Cosine")
      trig_choices= input("Enter choice(1/2):")
      if trig_choices == '1':
         print(sine_for_sides(num1, num2, num3))
      if trig_choices == '2':
         print(cos_for_sides(num1, num2, num3))
   elif options == '2':
      print("1.Sine")
      print("2.Cosine")
      angle_choices= input("Enter choice(1/2):")
      if angle_choices == '1':
         print(sine_for_angles(num1, num2, num3))
      if angle_choices == '2':
         print(cos_for_angles(num1, num2, num3))

   

