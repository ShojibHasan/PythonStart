'''
x = 1
y = 2.5
name = "Shojib"
is_cool  = True
print(x)
print(y)
print(name)
print(is_cool)

print(type(x))
print(type(y))
print(type(name))
print(type(is_cool))

'''

# Multiple assignmet
x, y, name, is_cool = (1, 2.5, 'Bari', True)
print(x, y, name, is_cool)
print(type(x), type(y), type(name), type(is_cool))

# basic Math
print("\n")
x, y = (1, 2.5)
sum = x + y
print("Result: ", sum)

multi = x * y
print("Multiplication: ", multi)

division = x / y
print("Division: ", division)

sub = x - y
print("Subsctration: ", sub)

# Casting / type conversation
x = str(x)
y = int(y)
z = float(y)

print(x)
print(y)
print(z)

# Type  of Variable
print(type(x))
print(type(y))
print(type(z))

x, y = (1, 2.4)
sum = x + y
print("Result: " + str(sum))

a = input("Enter a Nubmer")
b = input("Enter another Number")
result = a + b
print("Result is: ", result)

x = int(input("Enter a value"))
y = int(input("Enter another value"))
z = x + y
print(z)
