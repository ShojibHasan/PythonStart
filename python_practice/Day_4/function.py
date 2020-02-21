# function two types
#standerd function
def my_function():
    print("My name is Python")

def my_function():
    return "Python"


#not standerd
def myFunction():
    print("My name is python")

#function invok
my_function()

def my_function2(num_1,num_2): #paramerter
    return num_1+num_2
sum = my_function2(11,15) #argument
print(sum)

sum = my_function2(num_2=15,num_1=50)
print(sum)


def my_function3(num_1,name):
    return str(num_1) + name

sum = my_function3(num_1=15, name="Python")
print(sum)


def my_default(num1=200,num2=100):
    return num1+num2
sum1 = my_default(200)
print(sum1)

sum = my_default(200,1000)
print(sum)

def calculate(*num):
    sum = 0
    for i in num:
        sum +=i

    return sum
print(calculate(12,34,56,343,232))

def calculate(num1,num3,num2=100):
    return num1+num3+num2

def keyword_argument(**kwargs): #**kwargs = dictionary
    return kwargs
my_dict ={
    'age':12,
    'name':"python",
    'id':'123'
}
print(keyword_argument(**my_dict))

# function dictionary unpacking


def sub_sum(num1,num2):
    sum = num1+num2
    sub = num1-num2
    return sum,sub
a,b = sub_sum(100,500)
print(a,b)
print(sub_sum(100,500))