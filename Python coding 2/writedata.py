# import pickle
# l= [10, 20, 30, 40, 50]
# file=open("writedata.txt","wb")
# pickle.dump(l,file)
# file.close()



# num1=int(input("Enter the first number: "))
# num2=int(input("Enter the second number: "))
# print(num1+num2)

# count=5
# while(count>0):
#     print(count)
#     count=count-1

# n=int(input("Enter a positive integer: "))
# # initialize sum to 0
# sum=0
# # iterate over the range 1 to n and add each number to sum
# for i in range (1,n+1):
#     sum += i
# print("Sum of first",n,"natural number is: ",sum)
# # __________________________________________________________

# num=int(input("Enter a number: "))
# order=len(str(num))
# sum=0
# temp=num
# while temp>0:
#     digit=temp % 10
#     sum+=digit**order 
#     temp//=10
# if num==sum:
#     print(num,"is an Armstrong number")


# arr=[2,3,1,4,5,6,5,3,8,9,7,4]
# sorted_arr=sorted(arr)
# print(sorted_arr)


# arr=[2,4,3,5,6,7,7,8]
# largest_element=max(arr)
# print(largest_element)

# # create an array
# arr=[1,2,3,4,5,6,7,]
# # initialize a variable to store the sum
# sum=0
# # iterate over each element in the array and add it to the sum
# for i in arr:
#     sum+= i
# # print the sum of array elements
# print("Sum of array elements: ",sum)

# # define an array 
# arr =[1,2,3,4,5,6,7,8,9]
# # use the len() function to get the length of the array
# arr_length=len(arr)
# print("The number of elements in the array is:",arr_length)

# char=input("Enter a character: ")
# ascii_value=ord(char)
# print("The ASCII value of", char, "is", ascii_value)

# # take user input for a chracter
# char=input("Enter a character: ")
# # find the ASCII value using ord() function
# ascii_value=ord(char)
# # print the ASCII value
# print("The ASCII value of",char,"is", ascii_value)

# a=10
# b=5
# print(a/b)

# # divide without using divide operater
# x=float(input("Enter number X: "))
# y=float(input("Enter number Y: "))
# count=0
# while x>0:
#     x-=y
#     count += 1
# print(count)


# def factorial(x):
#     if x==1:
#         return 1
#     else:
#         return(x*factorial(x-1))
# num=int(input("Enter a number: "))
# result=factorial(num)
# print("The factorial of",num,"is",result)


# start=int(input("Enter number start: "))
# End = int(input("Enter number ending: "))
# a=0
# b=1
# fib_list=[]
# while a<= End:
#     if a>= start:
#         fib_list.append(a)
#         a, b = b, a+b
# print("fibonacci series within range:",fib_list)


# num1=float(input("Enter number First: "))
# num2=float(input("Enter number Second: "))
# num3=float(input("Enter number Third: "))

# if num1>num2 and num1>num3:
#     greatest = num1 
# elif num2>num1 and num2>num3:
#     greatest = num2
# else:
#     greatest = num3
# print("The greatest number is: ", greatest)


# a=5
# print(a,"is of type", type(a))

# a=3.0
# print(a,"is of type",type(a))

# a=1+2j
# print("is of type",type(a))

# s="This is a string"
# print(s)

# '''A multiline string'''
# print(a)

# s='Hello@123'
# print(s, type(s))

# s='''meri pyari maa'''
# print(s)

# l=[10,'sb',5.5]
# l[2]=10
# print(l,type(l))

# t= (10,38,'hello')
# t[l]=(10)

# print(t,type(t))

# d={
#     'course_name': 'python',
#     'course_duration':'2 Months'
# }
# print(d['course_name'])
# print(d,type(d))
# s={10,20,30,10}
# print(s,type(s))

# a = float(input("enter the value:- "))
# b = float(input("enter the value:- "))
# print(a+b)

# a = eval(input("enter the value1:- "))
# b = eval(input("enter the value2:- "))
# print(a+b)

# a = int(input("enter the value:-"))
# if a%2==0:
#     print(a,"even number")
# else:
#     print(a,"odd number")

# per = int(input("Enter the value"))
# if per>=60:
#     print("First Division")
# elif per>= 48:
#     print("Second Division")
# elif per>= 35:
#     print("Third Division")
# else:
#     print("Fail")

# print('''
# + Add,
# - Subtration,
# * Multiplation,
# / Divide
# ''')
# num1=int(input("Enter the value1: "))
# num2=int(input("Enter the value2: "))
# opr=input("Enter the opr..")
# if opr=="+":
#     print("num1+num2")
# elif opr=="-":
#     print("num1-num2")
# elif opr=="*":
#     print("num1*num2")
# elif opr=="/":
#     print("num1/num2")
# else:
#     print("invalid opr...")

# for n in range(5):
#     print("welcome ")

# for n in range(1,6):
#     print(n)

# for a in range(1,11):
#     print("2*",a,"=",2*a)

# for n in range(10,0,-1):
#     print(n)

# for n in range(10,4,-2):
#     print(n)

# i= 1
# while i<= 10:
#    print(i,"welcome to my home")
#    i=i+1
# print(i)

# a= 10
# while a>= 1:
#    print(a,"hello")
#    a = a-1
# print(a)
  
# w = "welcome to my Big House"
# print(w[8])
# print(w[-1])
# print(w[0:7])
# print(w[0::2])
# print(w[0::1])
# print(w[0::-1])
# print(w[-1::-1])
# t=len(w)
# print(t)
# for a in range(t):
#     print(w[a])


# print("")
# for a in range (t-1,-1,-1):
#     print(w[a])

# w = "mera"
# print(w.find('h',4))
# print(w.index('a'))

# print(w.isalpha())
# print(w.isdigit())
# print(w.isalnum())

# a = 67
# print(chr(a))
# a = 65
# print(chr(a))

# h = 'H'
# print(ord(h))

# w = "welcome{} to {} Shiv".format("hello",20);
# print(w)

# w ="welcome{0} to {1}Shiv".format("hello",20);
# print(w)

# w = "welcome {1} to {1} Shiv".format("hello",20)
# print(w)
# w = "welcome {1} to {0} Shiv".format("hello",20)
# print(w)

# w = "Welcome {a} to {b} Shiv".format(a=30,b=40);
# print(w)

# w = "Welcome {b:10} to {a} Shiv".format(a=30,b=20);
# print(w)

# w = "welcome {b:^10} to {a} Shiv".format (a=30,b=20);
# print(w)
# w = "welcome {b:<10} to {a} Shiv".format (a=30,b=20);
# print(w)
# w = "welcome {b:>10} to {a} Shiv".format (a=30,b=20);
# print(w)

# L = [2,3,"hello",[3,4,5]]
# print(L[2])
# print(L[0:2])
# print(L[1:])

# l = [1,2,3,4,5]
# print(l[0::2])
# print(l[-1::-1])
# t = len(l)
# for n in range(t):
#     print(l[n])
# for a in l:
#     print(a)

# l = [15,25,35,45,55,65,75,85,95]
# t = len(l)
# for n in range(t-1,-1,-1):
#     print(l[n])
# for a in range(t):
#     print (l[a])
# print(" ")
# for a in l:
#     print(a)

# l =[20,30,40]
# l.pop(2)
# print(l)

# l =[20,30,40,50,60]
# del l[1]
# print(l)

# l =[20,30,40,50,60]
# del l[1:4]
# print(l)

# l =[20,30,40,50,60]
# del l
# print(l)

# my_list = [1, 2, 3, 4, 5]
# del my_list

# l = [20,30,40,50,60]
# l.remove(60)
# print(l)

# l = [20,30,40,50,60]
# l.clear()
# print(l)

# l = [20,30,40,50,60]
# l[0] = 90
# print(l)

# l = [20,30,40,50,60]
# l.insert(0,10)
# print(l)

# l = [20,30,40,50,60]
# l.append(88)
# print(l)

# l = [20,30,40,50,60]
# n = [33,44,55]
# l.append(n)
# print(l)

# l = [20,30,40,50,60]
# n = [33,44,55]
# l.extend(n)
# print(l)

l = []
for a in range(1,101):
    l.append(a)
print(l)

n=[h for h in range (1,101)if h%2==0]
print(n)

