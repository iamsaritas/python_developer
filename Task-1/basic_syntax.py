# Variables
x = 5
y = "John"
print(x)
print(y)

# list
thislist = ["apple", "banana", "cherry"]
print(thislist)

# Arithmetic operators
print(10 + 5)

# Dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Strings
print("Hello")
print('Hello')

# Assign String to a Variable
a = "Hello"
print(a)

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Conditional statements
# If statement:
a = 33
b = 200
if b > a:
  print("b is greater than a")

# Elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# Else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# While Loops
  i = 1
while i < 6:
  print(i)
  i += 1

# break Statement
  i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Function
def my_function():
  print("Hello from a function")

my_function()