for i in range(10):
    print(i,end="\n")
print("-------- \n")
for i in range(1,10,2):
    print(i,"Hello World")

print("P" in "Python")

list_ =["Python","Programming","Language"]
for i in list_:
    print(i,end="\n")

age_dict = {
    'key': 'value',
    'karim': 20,
    'Abul': 20,
    'Kashem': 12,
}
for i in age_dict.items():
    print(i,end="\n")

for key, value in age_dict.items():
    print(key,":",value)

for i in age_dict.keys():
    print(i)

for j in age_dict.values():
    print(j)

for i in range(1,10):
    for j in range(i):
        print("*", end=" ")
    print()