set_1 = {1,3,5,7,9}
print(set_1)
print(type(set_1))

# add single item
set_1.add(2)
print(set_1.add(2))
print(set_1)

# add multiple items

set_1.update([12,22,43,78])
print(set_1)

# remove  item

set_1.remove(78)
print(set_1)

# union operation
set_2 = {100,200,300,13,34}
print( set_1 | set_2)

print(set_2.pop())
print(set_2.pop())
print(set_2.pop())

# remove
set_1.remove(9)
print(set_1)

# interaction

print(set_1 & set_2)

set_1.clear()
print(set_1)

