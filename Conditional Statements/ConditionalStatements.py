# If-Else Statements , Comparison Operators and Nested If-Else Statements

num = 10 

if num > 5:
    print("num is greater than 5")
elif num == 5:
    print("num is equal to 5")
else:
    print("num is less than 5")

# Logical Operators

x = 5
y = 10 

if x > 5 and y > 5:
    print("both conditions are true")
else :
    print("the condition here is False  ")

#  Project: Number Comparison Tool

user = float(input("Enter a number "))
user1 = float(input("Enter a number "))

if user > user1:
    print(f"{user} is greater than {user1}")
    
elif user == user1:
    print(f"{user} is equal to {user1}")
    
else:
    print(f"{user} is less than {user1}")
    
if user == 0 and user1 == 0 :
  print('both numbers are zero')
else:
  print('one number is not zero')



