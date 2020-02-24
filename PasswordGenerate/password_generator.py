import string
import random

letters = string.ascii_letters
#print(letters)

digts = string.digits
#print(digts)

punctuation = string.punctuation
#print(punctuation)

char = letters + digts + punctuation
#print(char)

password = random.choices(char,k=16)
#print(password) #it'll show list of 16 char
password = "".join(password)
print("Your Random Password is: ",password)

