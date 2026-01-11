# What are Variables ?
# Stock Data srting (ex: Name) , Integer (Number) ....

# Stoeing a name
name = 'med'
# Storing age
age = 25

# String
name = 'John'
# Ineger
age = 35 
height = 1,75
# Boolean
student = True 
print(type(name))
print(type(age))
print(type(height))
print(type(student))

# Type conversion
print('\n Type conversion')
x = '25'
Myage = int(x)
print(type(Myage))
print(Myage + 5)

# String Formatting
print('\n String Formatting')

friend1 = 'med'
friend2 = 'Jhon'
friend3 = 'alya'

print('Hello ' + friend1 + '!')
print('Welcome my friend {}!' .format(friend2))
print(f'Hello {friend3}')

# Project : Personakized Greeting Program
# Ask user
import datetime

UserName = input('Enter your name ')
Xname = UserName.lower()
Color = input('Enter your favorite color ')
Xcolor = Color.upper()
height = int(input('Enter your height '))
Xheight = float(height)
birth = int(input('Enter your birth year '))
Xbirth = datetime.datetime.now().year
# Generate a message
print(f'Hell Mr {Xname} your Favorite color is {Xcolor} and your height is {Xheight} cm ')
print(f'u age is {Xbirth - birth}')
