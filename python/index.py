my_list=[2,1,3,4,"aditya","neeraj","kumar"]
# print(my_list)
# print(max(my_list))
# print(min(my_list))
# print(sum(my_list))
# print(id(my_list))

# my_list.append("pathak")
# print(my_list)

# my_list.sort()
# print(my_list)

# my_list.extend("kumar")
# print(my_list)

# print(my_list)
# my_list.remove("kumar")
# print(my_list)

# my_list.clear()
# print(my_list)

# my_list.pop()
# print(my_list)
# my_list.insert(1,87)
# print(my_list)

# my_list.copy(l1)

# x=eval(input("enter first number"))
# y=eval(input("enter second number"))
# if x>y:
#     smaller=y
# else:
#     smaller=x
# for i in range(2,smaller+1):
#     if((x%i==0) and (y%i==0)):
#         hcf=i
# print("hcf will be:",hcf)       

# x=int(input("enter the range:"))
# sum=0
# for i in range(0,x+1):
#     sum=sum+i
# print(sum)    


# def display(*n):
#     sum=0
#     for i in n:
#         sum=sum+i
#     return sum

# print(display(1,2,3,4,5,6,7))

# def details(**n):
#     for k,v in n.items():
#         print(f"my{k} is {v}")
        
# details(name="aditya",city="bhopal")

# def details(**n):
#     print(n)
    
# details(name="neeraj",city="Bhopal")

# x=int(input("enter any number"))
# sum=0
# order=len(str(x))
# copy_x=x
# while(x>0):
#     last_digit=x%10
#     sum=sum+last_digit**order
#     x=x//10
# if(sum==copy_x):
#     print("armstrong number:",sum)
# else:
#     print("not armstrong:",sum)
    
# x=int(input("enter any number"))
# numb=x
# sum=0
# while(x>0):
#     digit=x%10
#     sum=sum*10+digit
#     x=x//10
# if(sum==numb):
#     print("palindrome number")
# else:
#     print("not palindrome")

# print("finding factorial")
# x=int(input("enter any number for factorial"))
# sum=1
# while(x>0):
#     sum=sum*x
#     x=x-1
# print("factorial is:",sum)

# x=int(input("enter any number for factorial"))
# num=1
# sum=1
# for i in range(x,2):
 
#     sum=i*i-1
# print(sum)

# n=int(input("enter the number of colums"))
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     print()
        
# n=int(input("enter column range"))
# for i in range(n):
#     for j in range(n-i):
#         print("*",end="")
#     print()
    

# n=int(input("enter the range column"))
# for i in range(n-1):
#     print(" ",end="")
    
# for j in range()
    
l1=[1,2,3,"aditya","aditya","sonal",10.5]
l2=["aditya","sonal","abdul","zaheed"]
l3=[1,2,3,4,5,6,70,8,9,10]


d1={"name":"aditya","surname":"pathak","rollno":"03"}
#d1.clear()
#d2=d1.copy()
#print(d1.get("name"))
#print(d1.items())
# d1.pop("surname")
# d1.popitem()

# import sys
# x=[1,2,3,4]
# print(sys.getsizeof(x))

# x=eval(input("enter first number"))
# y=eval(input("wenter second number"))
# if(x>y):
#     smaller=y
# else:
#     smaller=x
# for i in range(2,smaller+1):
#     if (x%i==0) and (y%i==0):
#         lcm=i
#         break
# print("LCM will be",i)
        
# x=10
# def funx():
#     print("value of x is",globals()["x"])
    
# funx()
        

# def sum(*x):
#     sum=0
#     for i in x:
#         sum=sum+i
#     return sum

# print(sum(1,2,2,3,4,5))

# def details(**n):
#     for k,v in n.items():
#         print(f"my {k} is {v}")
    
# details(name="aditya",rollno="03")

# def add(*x):
#     sum=0
#     for i in x:
#         sum=sum+i
#     return sum

# print(add(1,2,2,4,5))

# def new(**n):
#     print(n)
    
# new(name="neeraj",age=37,quali="37")

# armstrong number

# n=int(input("enter any number:"))
# sum=0
# order=len(str(n))
# copy_n=n
# while(n>0):
#     digit=n%10
#     sum=sum+digit**order
#     n=n//10
# if(sum==copy_n):
#     print("yes")
# else:
#     print("no")
    
# n=5
# for i  in range(n):
#     for j in range(i+1):
#         print("&",end="")
#     print()

# n=5
# for i in range(n):
#     for j in range(n-i):
#         print("*",end="")
#     print()

# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end="")
#     print()

# n=5
# for i in range(n):
#     for j in range(i):
#         print(" ",end="")
#     for j in range(n-i):
#         print("*",end="")
#     print()

# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(i):
#         print("*",end="")
#     for j in range(i+1):
#         print("*",end="")
#     print()


# n=int(input("enter any number:"))
# fact=1
# i=n
# while(i>=1):
#     fact=i*fact
#     i=i-1
# print(fact)

# print("check wheather the year is leap or not")
# n=int(input("enter the year"))
# if((n%4==0) and (n%100!=0)):
#     print("leap year")
# elif ((n%100==0) and (n%400==0)):
#     print("leap year")
# else:
#     print("not a leap year")
    
# l1=['name','aditya']
# str=''.join(l1)
# print(str)
    
    
# def display(word):
#     new_word=""
#     for i in word:
#         new_word=i+new_word
#     return new_word

# print(display("aditya"))

# def calculate(str):
#     digit_count,string_count=0,0
#     for letter in str:
#         if '0'<=letter<='9':
#             digit_count=digit_count+1
#         elif 'a'<=letter<='z' or 'A'<=letter<='Z':
#             string_count=string_count+1
#     print("dig count is",digit_count)
#     print("str count is",string_count)
    
# calculate("aditya234")
     
# n=int(input("enter a number:"))
# temp=n
# reverse=0
# while(n>0):
#     digit=n%10
#     reverse=reverse*10+digit
#     n=n//10
# if(temp==reverse):
#     print(f'{reverse} is a palindrome number')
# else:
#     print(f"{reverse} is not a palindrome number")

# str1=input("enter first number")
# str2=input("enter second number")
# if (sorted(str1)==sorted(str2)):
#     print("anagram")
# else:
#     print("not anagram")       



# a=input("enter any word")
# vowel=0
# consonant=0
# for i in range(0,len(a)):
#     if (a[i]!=""):
#         if (a[i]=='a'or a[i]=='e',a[i]=='i',a[i]=='o',a[i]=='u'):
#             vowel=vowel+1
#         else:
#             consonant=consonant+1
# print("vowels are",vowel)
# print("conso are:",consonant)
    
#------------------------Advance python

# def cube(x):
#     return x*x*x

# l=[1,2,3,4,5,6,7,8,9]

# new=map(cube,l)
# print(tuple((new)))

# def square(x):
#     return x**2

# n=eval(input("enter any list"))
# res=map(square,n)
# print(list(res))

# def display(x):
#     if x%2==0:
#         return x+1
#     else:
#         return x+2
    
# n=eval(input("enter any list"))
# print(list(map(display,n)))

# def display(x,y,z):
#     return x+y+z

# l1=[2,4,6]
# l2=[1,2,3]
# l3=[4,7,2,8,6,9,10]
# res=map(display,l1,l2,l3)
# print(list(res))

# def new(x):
#     return x>4

# l1=[1,2,3,4,5,6,7,8,9,10]
# res=filter(new,l1)
# print(list(res))

# from functools import reduce

# def display(x,y):
#     return x+y
# l1=[1,2,3,4,5,6,7,8,9,10]
# l2=[1,2,3,4,5,6,7]
# result=reduce(display,l1)
# print(result)

# l1=[1,2,3,4,5,6]
# l2=[6,5,7,5,8,9]
# x=map(lambda x,y : x**2+y**2,l1,l2)
# print(list(x))

# decorators

# def greet(milf):
#     def xc(): 
#        print("good morning")
#        milf()
#        print("thanks for using")
#     return xc

    
    
# @greet    
# def display():
#     print("hello world")
    
# display()
# @greet
# def add(a,b):
#     print(a+b)
    
# add(1,2)
    

    
# class Book:
#     def welcome(self):
#         print("welcome to our library")
     
#     @staticmethod    
#     def thanks():
#         print("thanks for visit")
    
# obj=Book()
# obj.welcome()
# obj.thanks()


# from abc import ABC,abstractmethod

# class Computer(ABC):
#     @abstractmethod
#     def animal(self):
#         pass
# class cat_family(Computer):
#     def cat(self):
#         print("meow")
        
# class dog_family(Computer):
#     def cat(self):
#         print("Bark")
        
# c1=cat_family()
# c1.cat()

# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         print("Woof!")

# class Cat(Animal):
#     def make_sound(self):
#         print("Meow!")


# #dog = Dog()
# cat=Cat()
# cat.make_sound()     # Output: Woof!

# from abc import ABC,abstractmethod

# class BankApp(ABC):
#     def login(self):
#         print("login")
#     def logout(self):
#         print("logout")
#     def details(self):
#         print("user details")
#     @abstractmethod
#     def database(self):
#         pass
    
# class WebPage(BankApp):
#     def database(self):
#         print("database connected")
        
# w1=WebPage()
# w1.login()
# w1.logout() 
# w1.details()
# w1.database()   
    
    
# from abc import ABC,abstractmethod

# class BankApp(ABC):
#     def login(self):
#         print("self login")
#     def logout(self):
#         print("logout")
#     def details(self):
#         print("details")
        
#     @abstractmethod
#     def database(self):
#         pass

# class WebPage(BankApp):
#     def database(self):
#         print("database printed")
        
# obj=WebPage()
# obj.login()
# obj.logout()
# obj.details()
# obj.database()

# class A:
#     name="aditya"
#     city="bhopal"
#     def __init__(self):
#         age=22
#         print(self.name)
#         print(self.city)
#         print(age)
      
       
    
 
        
# obj=A()

# class A:
#     def __init__(self,name,age,city):
#         city="bhopal"
#         print(name,age,city)
        
# obj=A("aditya",24,None)
        
# class B:
#     def __init__(self):
#         def new():
#             print("finction inside constructor")
            
# obj=B()
        
# class A:
#     def __init__(self,value):
#         self.value=value
        
#         def inner(self):
#             return self.value*2
#         self.calculate=inner(self)
        
# obj=A(2)
# print(obj.calculate)

# class A:
#     x=10
#     y=20
#     def home(self):
#         print("have a home")
#     def car(self):
#         print("my car")
        
# class B(A):
#     def new(self):
#         print("have indian")

# obj1=B()
# print(obj1.home())
# print(obj1.new())
# print(obj1.car())

# single inheritance

# class Parent:
#     def fun(self,name):
#         print("im parent")
#         self.name=name
        
# class Child(Parent):
#     def fun1(self):
#         print("im child")
#         print(self.name)
        
        
# c1=Child()
# c1.fun("aditya")
# print(c1.fun1())

# class Parent:
#     x=10
#     def car(self):
#         print("parent class")
        
# class Child(Parent):
#     def car(self):
#         super().car()
#         print("child class")
        
# obj=Child()
# print(obj.car())
        
# multiple inheritance

# class Parent1:
#     def home(self):
#         print("parent-1")
        
# class Parent2:
#     def city(self):
#         print("parent-2")
        
# class Child(Parent1,Parent2):
#     def car(self):
#         print("child car")
        
# obj=Child()
# obj.city()
# obj.home()

# multilevel inheritance

# class first:
#     def home(self):
#         print("first")
        
# class second(first):
#     def city(self):
#         print("second")
        
# class third(second):
#     def state(self):
#         print("third")
        
# t1=third()
# t1.home()
# t1.city()

# class Chasis:
#     def basic(self):
#         print("chasis")
        
# class Engine(Chasis):
#     def basic(self):
#         super().basic()
#         print("engine")
        
# class Body(Engine):
#     def basic(self):
#         print("car Body")
        
# b1=Body()
# b1.basic()

#----H

# class Parent:
#     def __init__(self,name,age):
#             self.name=name
#             self.age=age
#             print("Parent Class")

        
# class Child1(Parent):
#     def city(self):
#         print("child 1")
    
# class Child2(Parent):
#     def state(self):
#         print("state MP")
        
# obj=Child2()
# obj.home()
from time import sleep
from threading import Thread
class A(Thread):
    def show(self):
        for i in range(5):
            print("aditya")
            sleep(1)
            
class B(Thread):
    def show(self):
        for i in range(5):
            print("shivi")
            sleep(1)
        
        
obj=A()
obj1=B()
obj.start()
obj1.start()



        


        