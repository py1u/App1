#Python Notes

#printing something readable to terminal output, print creates a newline after whatever is outputed
#print is a built in function in python, all functions must be called or written in lowercase, Ex: print() get() set() etc.
print("Hello World")


#variables can be declared and initialized like this, if you want space in variable name use "_", and no numbers at the start
x1 = 10
print(x1)

use_underscore_as_space = "Use underscore as a space"

#no type is needed to be set when creating a variable, and variables can change datatypes
x2 = 10
x2 = "String"
print(x2)

#you can specify datatype of variable if you want
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#get datatype of variable with type() function
print(type(x))
#type wont return datatype to output, encapsulate it in print() function

#declare string quotations as single or double, your preference
x = "John"
# is the same as
x = 'John'

#multiple variable declaration and assignment on one line

x3,x4,x5 = "apple", 30, 'c'
print(x3)
print(x4)
print(x5)

#or mutiple variables, same value
x6 = x7 = x8 = "Orange"
print(x6)
print(x7)
print(x8)

#python can unpack a list
fruits = ["apple", "banana", "cherry"]
x9, x10, x11 = fruits
print(x9)
print(x10)
print(x11)

#print mutiple variables seperated by , OR + in code, a space in output
x = "Python"
y = 10
z = 5.0
print(x, y, z)
#print(x + y + z) BUT + can only be used for the same data type
a = "This "
b = "is"
c = "Python Programming"
print(a + b + c) #note the space inside the quote that gave proper spacing but not after "is"
# best to output multiple values in print with commas


globalVariable = 5
# functions start with def, variablename() :
def globalGetter():
    print("the global variable value is", globalVariable)

globalGetter() #this is how to call a function after creation

#if you declare a variable outside a function, its global, any function can use it,
#otherwise a variable declared inside a function is local, only exists in the function when it is run

x = "awesome" #global variable

def myfunc():
  x = "fantastic" #local variable so it doesnt update global x, its like a new x
  print("Python is " + x)

myfunc()

print("Python is " + x)
x = "fun" #now this updates the global variable x
print("Python is " + x)

# use global variablename if you wanna declare a global variable inside a function, or update global variable outside the function


#using str() is typecasting, turning age from int to string
age = 21
age += 3
print("your age is:" + str(age))


height = 230.9
print("your height is:" , str(height) , "cm")
print("the data type for variable height is:", type(height))

user input
age = input("How old are you?\n")
new_age = float(input("What is your age? ")) + 1 #typecast age into age to do math operations
print("In a year you will be " + str(new_age) + " years old.")# typecast new_age into string for print statment


height = float(input("how tall are you? "))
print("You are " + str(height) + "cm tall")

import math

pi = 3.14
x = 1
y = 2
z = 4
#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(-7))
#print(pow(pi,2))
#print(math.sqrt(64))
print(max(x,y,z))
print(min(x,y,z))

string slicing

name = "Peter Lu"
first_name = name[0:5]
last_name = name[6:8]
funky_name = name[::3]
print(funky_name)

reversed_name = name[::-1]
print(reversed_name)

website_url = "http://google.com"
slice = slice(7, -4)
print(website_url[slice])

website_url2 = "http://wikipedia.com"
print(website_url2[slice])

age = int(input("what is your age?\n"))


if age >= 18:
    if age == 100:
        print("you are old")
    else:
        print("you are are an adult!")
elif age < 0:
    print("you havent been born yet")
else:
    print("you are a child")

temp = int(input("what is the temperature outside?: "))

if not(temp >= 0 and temp <= 30):
    print("temperature is bad today, stay home.")

elif not(temp < 0 or temp > 30):
    print("the temperature is good today, go outside.")

name = None

while not name:
    name = input("enter a name:")

print("Hello " + name)


for i in range(5):
    print(i+1)


for i in range(50,101,10):
    print(i)

for i in "Peter Lu":
    print(i)

import time

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)

print("Happy New Year")

# f strings used for simpler string interpolation with variables
number = 13
print(f"this number is {number}")

#lets say item = apple
f"{index}).{item}" which prints 0.apple

#the enumerate function
enumerate(list_name)
#requires two indexing variables: i,j
#i prints the index of the array, j prints the actual item

#you can use more than two indexing variables:
buttons = [('John', 'Sen', 'Morro'), ('Lin', 'Ajay', 'Filip')]
for first, second, third in buttons:
    print(first, second, third)
#output would be  John Sen Morro and Lin Ajay Filip in second line right below

# lists vs arrays
# both have the same initalization: variable_name = [some data]
# main difference is list can have items of different data types, array only has same data types

#lets write to a file to store basic user items as data
file = open('todos.txt', 'w')
# first string is the file directory, second string is w for write
file.writelines(todos)
#writelines() is a method that will write to your txt file

open() #will create a new file if it doesn't exist, it if already exists, it will override the old folder
write() #dont produce newlines unless stated with newline '\n'

#
zip() #is similar to enumerate() but instead with two lists it will allow you to group a item, item instead of index,item

read() # reads a entire file as a string
readline() # reads a single line in a file

#how to modify a list into shorter newline sections:
goals = ["LeetCode easy 1 a day",
         "Network 5 people, and apply 10 jobs",
         "Work on Artr Login page"]
#can be done with a single long string as well:
intro = "Hello, this is a " \
        "file for python notes"

strip() #a method that removes a character from a string when specified ex.
strip('\n') # will remove the newline inside a string

'''
comment tip: only comment when you want to
tell something useful to a programmer, not what does the syntax mean
 or what the function is doing
'''

new = []

for i in [1, 2, 3]:
    new.append(i + 10)

print(new)

# A list comprehension can't always do the same thing a for-loop does,
# but when it does, the list comprehension becomes the preferred method since it uses less code.

old = [1,2,3]
new = [i + 10 for i in old]
print(new)

# another example:

names = ["john smith", "jay santi", "eva kuki"]

new_names = []
for index in range(len(names)):
    new_name = names[index].title()
    new_names.append(new_name)

print(new_names)

#using list comprehension reduces our code
names = ["john smith", "jay santi", "eva kuki"]
names = [item.title() for item in names]
print(new_names)

#case where we use assignment operator inside a expression, so = becomes :=

user_entries = ['10', '19.1', '20']
sum = 0.0
user_entries = [sum := sum + float(item) for item in user_entries]
print(sum)
# sum is 49.1