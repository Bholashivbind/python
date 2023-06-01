# class DemoClass:
#     a=10

#     def sumvalue(self):
#         print(20+30)


# demoobject=DemoClass()
# demoobject1=DemoClass()
# print(demoobject.a)
# print(demoobject1.a)
# demoobject.sumvalue()

# class demoClass:
#     a=10
#     def showvalue(self):
#         self.c=self.a*self.a
#         print(self.c)
#     def showvalue1(self,a,b):
#         print(a+b)
# obj=demoClass()
# obj.showvalue()
# obj.showvalue1(40,68)

# class demoClass:
#     a=10
#     def __init__(self) -> None:     # constructor
#         print("Welcome to Shiv Bhola laptop")
#     def showvalue(self):
#         self.c=self.a*self.a
#         print(self.c)
#     def showvalue1(self,a,b):
#         print(a+b)
# obj=demoClass()
# obj.showvalue()
# obj.showvalue1(40,68)

                     #  inheritance
# class A:
#     def displayA(self):
#         print("Welcome to Home A")
# class B(A):
#     def displayB(self):
#        print("Welcome to Home B")

# obj=B()
# obj.displayA()
# obj.displayB()


# class A:
#     def displayA(self):
#         print("Welcome to Home A")
# class B(A):
#     def displayB(self):
#        print("Welcome to Home B")
# class C(B):
#     def displayC(self):
#        print("Welcome to Home C")
# obj=C()
# obj.displayA()
# obj.displayB()
# obj.displayC()
                     
                     # multiple inheritance
# class A:
#     def displayA(self):
#         print("Welcome to Home A")
# class B:
#     def displayB(self):
#        print("Welcome to Home B")
# class C(A,B):
#     def displayC(self):
#        print("Welcome to Home C")
# obj=C()
# obj.displayA()
# obj.displayB()
# obj.displayC()

                    # Encapsulation
# class Student:
#     def __init__(self):
#         self.__name=""
#     def getname(self):
#         return self.__name
#     def setname(self,name):
#         self.__name=name
# obj=Student()
# obj.setname("Testing")
# name=obj.getname()
# print(name)


# class Student:
#     __name="Bhola"
#     def __init__(self):
#         print(self.__name)
#     def __displayinfo(self):
#         print("Welcome to  my heart🥰")

# obj=Student()

                 # polymorphism
# l = [10,20,30,40,50]
# print(len(l))       #  ->  l
# s = "welcome"
# print(len(s))         # ->  s

                # polymorphism _ *oevrloading* _
# class Sb1:
#     def findarea(self,a=None,b=None):
#         if a!=None and b!= None:
#             print("Area of Rectangle:",(a*b))
#         elif a!=None:
#             print("Area of square:",(a*a))
#         else:
#             print("Nothing to find")
# obj=Sb1()
# obj.findarea()
# obj.findarea(10)
# obj.findarea(10,20)

                  
# class Sb:
#     def displayinfo(self, name=''):
#         print("Welcome to  my heart🥰"+name)
# obj= Sb()
# obj.displayinfo()
# obj.displayinfo(' Jay Prakash')


                   # polymorphism _ *oevrloading* _
# class Sb:
#     def displayinfo(self):
#         print("Welcome to  my heart🥰")
# class Sbb(Sb):
#     def displayinfo(self):
#         super().displayinfo()
#         print("Welcome to  Villege 🥰")
# obj=Sbb()
# obj.displayinfo( )

class A:
    def showData(self):
        print("I am in A class")
class B(A):
    def showData(self):
        print("I am in B class")

obj=B()
obj.showData()











