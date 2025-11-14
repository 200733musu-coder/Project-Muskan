# print("Hello World")
# #if else

# age=16

# if age>18:
#     print("you are adult")
    
# elif age==18:
#     print("you are teen")

# elif age==17:
#     print("you are 17")

# elif age==16:
#     print("you are 16")
# else:
#     print("you are not adult")


# x=15

# if x>10:
#     print("x is greater than 10")

#     if x>20:
#         print("x is greater than 20")

#     else:
#         print("x is not greater than 20")

#         x=7

#         if x%2!=0:
#             print("this number is odd")

#         else:
#             print("this number is even")




# a=20

# if a>=18:
#     print("eligible for driving")

# else:
#     print("not eligible for driving")

# fruits=["apple","banana","cherry"]

# for fruit in fruits:
#     print(fruit)

# word = "python"

# for letter in word:
#     print(letter)

# for i in range(5):
#     print(i)


# for i in range(1,10,2):
#     print(i)

# for i in range(1,4):
#     for j in range(1,3):
#         print(f"i={i},j={j}")

# for i in range(1,6):
#     if i==4:
#         break
#     print(i)

# for i in range(1,6):
#     if i==3:
#         continue
#     print(i)

# for i in range(1,4):
#     print(i)
# else:
#     print("Loop is finished")

# for i in range(1,21):
#     print(i)

# for i in range(2,30,2):
#     print(i)

# colors = ["blue","pink","yellow"]
# for color in colors:
#     print(color)

# for i in range(1,11):
#     if i==5:
#         continue
#     print(i)

# def greet():

#     print("Hello Python!")

# greet() #calling the function

# def greet(name):
#     print(f"Hello,{name}!")
# greet("Alice")
# greet("Bob")

# def add(a,b):
#     return a+b
# result=add(5,3)
# print(result) #8

# class Car:
#     def __init__(self,brand,color):
#         self.brand=brand
#         self.color=color
#     def drive(self):
#         print(f'{self.color} {self.brand} is driving')
# car1=Car("bmw" , "black")
# car1.drive()

# import array

# numbers=array.array('i',[1,2,3,4,5])
# print(numbers)

# from numpy import random
# x = random.randint(100)
# print(x)


# x = random.rand()
# print(x)

# x=random.randint(100,size=(5))
# print(x)

# x=random.randint(100,size=(3,5))
# print(x)

# x=random.randint(100,size=(2,3,5))
# print(x)

# x=random.randint(100,size=(2,2,3,5))
# print(x)

# x=random.choice([4,5,6], size=(5))
# print(x)

#pandas

# import pandas as pd 

# data=[10,20,30,40]
# s=pd.Series(data)

# print(s)
# 4


# import pandas as pd

# data={
#     "Name":["Alice","Bob","Charlie","David"],
#     "Age":[24,27,22,32],
#     "City":["Delhi","Mumbai","Chennai","Kolkata"]
# }

# df=pd.DataFrame(data)

# print(df)


# import numpy as np

# arr=np.array([1,2,3,4,5])
# s=pd.Series(arr)
# print(s)

# data={"Math":90,"Science":85,"English":78}
# s=pd.Series(data)
# print(s)

