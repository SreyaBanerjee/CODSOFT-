
import random
import string
#Taking the user input to specify the length of the characters
len = int(input("Enter the length of the password"))
#Assigning the digits, letters and symbols
str=string.ascii_letters
str+=string.punctuation
str+=string.digits
#Initialising the Password Variable
password = " "
for i in range(len):
    nxt_str = random.choice(str)
    password+= nxt_str
#Display the Password
print("Hey User: Your password is:", password)