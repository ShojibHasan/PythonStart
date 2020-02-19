# A data structure of python

dict_1 = {} # Not set
dict_2 = dict()
print(type(dict_1))
print(type(dict_2))

age_dict = {
    'key': 'value',
    'karim': 20,
    'Abul': 20,
    'Kashem': 12,
}

print(age_dict)
print(age_dict.items())
print(age_dict.keys())
print(age_dict.values())

print(age_dict['Abul'])
print(age_dict.get('abul'))

print(age_dict.get('Kashem'))
age_dict['python'] = 100

print(age_dict.items())