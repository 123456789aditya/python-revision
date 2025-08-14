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

x=eval(input("enter first number"))
y=eval(input("wenter second number"))
if(x>y):
    smaller=y
else:
    smaller=x
for i in range(2,smaller+1):
    if (x%i==0) and (y%i==0):
        lcm=i
        break
print("LCM will be",i)
        
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

def details(**n):
    for k,v in n.items():
        print(f"my {k} is {v}")
    
details(name="aditya",rollno="03")
