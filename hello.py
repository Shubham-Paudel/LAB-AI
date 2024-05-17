# print("Hello, World!!")

# name = "Shubham"

# print(type(name))

# '''
# First
# AI
# Lab
# '''

# print(f"I am {name}")

# first = 2
# second = 3
# print(first + second)
# print(first - second)
# print(first * second)
# print(first // second)
# print(first ** second)

# sum = 0
# sum += 1

# print(type(first == second))

# name = input("Enter your name : ")
# print(name)
# print(type(name))

# age = input("Enter your age : ")
# print(age)
# print(type(age))

# nationality = input("Your nationality : ")
# if(nationality == "Nepali"):
#     if(int(age) < 14):
#         print("You are a minor")
#     elif(int(age)>18):
#         print("You are eligible")
# else:
#     print("You are not eligible")
sum = 0

for i in range(1,11):
    sum+=i
print(sum)
i=0
sum=0
while(i<11):
    sum+=i
    i+=1
print(sum)

def add(a=5,b=3):
    print(a+b)

add(2,7)
add()
add(2)
