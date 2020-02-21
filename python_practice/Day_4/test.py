x = 300
y = 300

print(x is y)

x = 256
print(id(x))
y = 256
print(id(y))

x = 257
print(id(x))
y = 257
print(id(y))