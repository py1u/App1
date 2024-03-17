# #Python Notes

# #printing something readable to terminal output, print creates a newline after whatever is outputed
# #print is a built in function in python, all functions must be called or written in lowercase, Ex: print() get() set() etc.
# print("Hello World")


# #variables can be declared and initialized like this, if you want space in variable name use "_", and no numbers at the start
# x1 = 10
# print(x1)

# use_underscore_as_space = "Use underscore as a space"

# #no type is needed to be set when creating a variable, and variables can change datatypes
# x2 = 10
# x2 = "String"
# print(x2)

# #you can specify datatype of variable if you want
# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(3)  # z will be 3.0

# #get datatype of variable with type() function
# print(type(x))
# #type wont return datatype to output, encapsulate it in print() function

# #declare string quotations as single or double, your preference
# x = "John"
# # is the same as
# x = 'John'

# #multiple variable declaration and assignment on one line

# x3,x4,x5 = "apple", 30, 'c'
# print(x3)
# print(x4)
# print(x5)

# #or mutiple variables, same value
# x6 = x7 = x8 = "Orange"
# print(x6)
# print(x7)
# print(x8)

# #python can unpack a list
# fruits = ["apple", "banana", "cherry"]
# x9, x10, x11 = fruits
# print(x9)
# print(x10)
# print(x11)

# #print mutiple variables seperated by , OR + in code, a space in output
# x = "Python"
# y = 10
# z = 5.0
# print(x, y, z)
# #print(x + y + z) BUT + can only be used for the same data type
# a = "This "
# b = "is"
# c = "Python Programming"
# print(a + b + c) #note the space inside the quote that gave proper spacing but not after "is"
# # best to output multiple values in print with commas


# globalVariable = 5
# # functions start with def, variablename() :
# def globalGetter():
#     print("the global variable value is", globalVariable)

# globalGetter() #this is how to call a function after creation

# #if you declare a variable outside a function, its global, any function can use it,
# #otherwise a variable declared inside a function is local, only exists in the function when it is run

# x = "awesome" #global variable

# def myfunc():
#   x = "fantastic" #local variable so it doesnt update global x, its like a new x
#   print("Python is " + x)

# myfunc()

# print("Python is " + x)
# x = "fun" #now this updates the global variable x
# print("Python is " + x)

# # use global variablename if you wanna declare a global variable inside a function, or update global variable outside the function


# #using str() is typecasting, turning age from int to string
# age = 21
# age += 3
# print("your age is:" + str(age))


# height = 230.9
# print("your height is:" , str(height) , "cm")
# print("the data type for variable height is:", type(height))

# user input
# age = input("How old are you?\n")
# new_age = float(input("What is your age? ")) + 1 #typecast age into age to do math operations
# print("In a year you will be " + str(new_age) + " years old.")# typecast new_age into string for print statment


# height = float(input("how tall are you? "))
# print("You are " + str(height) + "cm tall")

# import math

# pi = 3.14
# x = 1
# y = 2
# z = 4
# #print(round(pi))
# #print(math.ceil(pi))
# #print(math.floor(pi))
# #print(abs(-7))
# #print(pow(pi,2))
# #print(math.sqrt(64))
# print(max(x,y,z))
# print(min(x,y,z))

# string slicing

# name = "Peter Lu"
# first_name = name[0:5]
# last_name = name[6:8]
# funky_name = name[::3]
# print(funky_name)

# reversed_name = name[::-1]
# print(reversed_name)

# website_url = "http://google.com"
# slice = slice(7, -4)
# print(website_url[slice])

# website_url2 = "http://wikipedia.com"
# print(website_url2[slice])

# age = int(input("what is your age?\n"))


# if age >= 18:
#     if age == 100:
#         print("you are old")
#     else:
#         print("you are are an adult!")
# elif age < 0:
#     print("you havent been born yet")
# else:
#     print("you are a child")

# temp = int(input("what is the temperature outside?: "))

# if not(temp >= 0 and temp <= 30):
#     print("temperature is bad today, stay home.")

# elif not(temp < 0 or temp > 30):
#     print("the temperature is good today, go outside.")

# name = None

# while not name:
#     name = input("enter a name:")

# print("Hello " + name)


# for i in range(5):
#     print(i+1)


# for i in range(50,101,10):
#     print(i)

# for i in "Peter Lu":
#     print(i)

# import time

# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)

# print("Happy New Year")

# f strings used for simpler string interpolation with variables
number = 13
print(f"this number is {number}")