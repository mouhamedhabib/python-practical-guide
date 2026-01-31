# for i in range (start, end, step):
#     # bloc d'instructions


for i in range(1 , 5 , 1):
    print(i)

# while condition:
# bloc d'instructions
print("while") 
count = 5 
while count > 0:
    print(count)
    count -= 1

# time
import time 
for i in range(5, 0, -1):
    print(i)
    time.sleep(0.1)
print("Go!")


user = int(input("Enter a  number: "))

for i in range(user , 0 , -1):
    print(i)
    time.sleep(0.5)
print("Done!")


start = int(input("Enter the start number: "))
while start >= 0:
    print(start)
    start -= 1
    time.sleep(0.5)
print("Finished!")

starts = int(input("Enter the start number: "))
delay = float(input("Enter the delay time in seconds: "))
while starts >= 0:
    print(starts)
    starts -= 1
    time.sleep(delay)
print("Finished!")
