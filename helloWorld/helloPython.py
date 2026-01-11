import datetime

# What is a print statement?
print ('hello Python world')

# How to use print with text and numbers
print('hello med')
print('2 + 2 = ' , 2+2)# dont forget , or + after ' ' 

# String formatting for dynamic messages
# Software base use f'{variable}'
name='med'
print(f'hello {name}')

# Using user input with print
# Software base
# variable = input('value')
# print(f'{variable}')
userNmae = input('enter your name ')
print(f"hello {userNmae} welcome to python course")

# Project: Welcome Message Generator
# welcome message
# step 1 ask user for name and hobby
# step2 generate message welcome
print("\n ---- welcome ------")  # welcome message
# step 1 ask user for name and hobby
userName = input('enter your name ')
hobby = input('enter your hobby ')
nom = userNmae.lower()
time = datetime.datetime.now()
# step2 generate message welcome
print(f"welcome {nom} It was great getting to know you like {hobby}\n {time}" )
