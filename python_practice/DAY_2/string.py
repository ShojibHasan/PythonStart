Firstname = "Python"
lastName = "Is A Programming Language"
number_1 = 24.00
print(" "+Firstname+" "+lastName+" \n Batch:"+ str(number_1))

print('{},{},{}'.format("a","b","c"))
print('{1},{2},{0}'.format("a","b","c"))

name_1 = "Python"
version = 3.7
# Python version 3.0 to 3.5
print("This is {python} programming Language.version is {version}".format(python=name_1,version=version))
print("This is {python} programming Language.version is {version}".format(python="Python",version=3.7))

# Python version 3.6 to 3.8
print(f'This is {name_1} programming Language. Version is {version}')

name = "python language"
print(name.capitalize())
print((name.title()))
print(name.upper())
print(name.lower())
print(name.swapcase())
print(name.split())

list_1 =[]
list_2 = list(("python","Python",1,3.6,True,False))
list_3 =["python","Python",1,3.6,True,False]

list_1.append(1)
print(list_1)
list_1.extend([list_2])
print(list_1)

list_1.extend(list_2)
print(list_1)

list_3.insert(0,"Language")
print(list_3)

fruits =['Apples',"Orange",'Grapes','Banana']
print(fruits)
print(fruits[1])
print(fruits[2])
print(len(fruits))
fruits.remove('Orange')
print(fruits[:])

fruits.reverse()

fruits.sort()
fruits.sort(reverse=True)
print(fruits[:])
print(fruits[0:])
print(fruits[:2])

print(fruits[::2])
print(fruits[::-1])

print(fruits[::-2])

