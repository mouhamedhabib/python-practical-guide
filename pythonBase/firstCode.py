name = 'med'
age = 25 
height = 175 
is_gamer = True 

print ('name' , name)
print ('age' , age)
print ('height' , height)
print ('is_gamer' , is_gamer )

userName = input('your name pls ')
user_name = userName.strip()
print('hello', user_name)

# Mat
print("Mat\n")  # \n here for new line 
x = 3 
y = 10 

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(x % y)
print(x ** y)

print("Condition if Else Elif\n")

age = int(input("Enter your age "))  # int() Function convert string value to Number 
if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
else:
    print('You are minor')

print("Loops Repaiting Action \n")

count = 0  # start count from 0
while count < 5:  # repeat the loop while count is less than 5
    print("count", count)  # print the current value of count 
    count = count + 1  # add plus 1 to count and go to check count if count < 5 or no . 
    # if no repeate

# list
games = ['game 1', 'game 2', 'game 3']
for game in games:
    print(game)


print("Lists stuff \n")
print(games[0]) #print index 0 inside the list 
games.append('game 4') # add new value in list in the last index like here index 4 
games[0] = 'call of duty' # here we rename index 0 frome game 1 to call of duty 
print(games)

print("function \n")

def fristFunction():
  print('hello from your first function ')
fristFunction()

print("function + parameter \n")

def persone(name):
  print('hello ' + name + ' and welcome to your space ')
persone('med')

def multiply(a,b):
  return a*b 
result = multiply(2,3)
print(result)

print("mini project \n")
# Number guessing game
# START

# SET computerNumber ← random number between 1 and 10
# SET attempts ← 3

# WHILE attempts > 0 DO
#     ASK user to enter a number
#     READ userNumber

#     IF userNumber = computerNumber THEN
#         DISPLAY "Good job"
#         STOP the loop
#     ELSE IF userNumber < computerNumber THEN
#         DISPLAY "Too low"
#     ELSE
#         DISPLAY "Too high"
#     END IF

#     attempts ← attempts - 1
# END WHILE

# IF attempts = 0 THEN
#     DISPLAY "You lost, try again later"
#     DISPLAY "The computer number was", computerNumber
# END IF

# END


import random 
computerThink = random.randint(
    1, 10
)  # The randint() method returns an integer number selected element from the specified range.
att = 3

while att > 0 :
  humain = int(input('enter what u think and rember u have 3 try '))
  if computerThink == humain :
    print('good job')
    break
  elif humain < computerThink:
    print ('too low')
  else:
    print('too high')
  att = att - 1
if att == 0 :
  print('you lost try again later and this what computer think' , computerThink )
    
