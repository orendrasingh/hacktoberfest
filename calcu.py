# import math
#
# # with contructor
#
# class Calculator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self,a,b):
#         self.a=a
#         self.b=b
#         return a+b
#     def sub(self,a,b):
#         self.a=a
#         self.b=b
#         return a-b
#     def div(self,a,b):
#         self.a=a
#         self.b=b
#         return a/b
#     def floor(self,a,b):
#         self.a=a
#         self.b=b
#         return math.floor(a/b)
#     def ceil(self,a,b):
#         self.a=a
#         self.b=b
#         return math.ceil(a/b)
# ad=Calculator(1,1)
# c=ad.add(7,8)
# e=ad.ceil(7,8)
# f=ad.floor(7,8)
# d=ad.div(7,8)
# print("without constructor","\n","Add = ",c)
# print("ceil = " ,e)
# print("floor = ", f)
# print("div = ",d)
#
# #without contructor
#
# class Calculator:
#     def add(self,a,b):
#         self.a=a
#         self.b=b
#         return a+b
#     def sub(self,a,b):
#         self.a=a
#         self.b=b
#         return a-b
#     def div(self,a,b):
#         self.a=a
#         self.b=b
#         return a/b
#     def floor(self,a,b):
#         self.a=a
#         self.b=b
#         return math.floor(a/b)
#     def ceil(self,a,b):
#         self.a=a
#         self.b=b
#         return math.ceil(a/b)
# ad=Calculator()
# c=ad.add(5,7)
# e=ad.ceil(7,8)
# f=ad.floor(7,8)
# d=ad.div(7,8)
# print(" without constructor","\n","Add = ",c)
# print("ceil = " ,e)
# print("floor = ", f)
# print("div = ",d)
#
# #use for just empty class
# class Calc:
#     pass
# def add():
#     pass

class Cal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def full(self,last):
        self.last=last
        return self.name,self.last
    def shor(self):
        return self.name[0]

obj=Cal('ram',23)
print(obj.full('sharma'))

print(obj.shor())
print(obj.name)

# dendrum var
class Cal:
    def __init__(self,_name,age):
        self._name=_name
        self.age=age
    def full(self,last):
        self.last=last
        return self._name,self.last
    def shor(self):
        return self._name[0]

obj=Cal('ram',23)
print(obj.full('sharma'))

print(obj.shor())
print(obj._name)

# double dendrum

class Cal:
    def __init__(self,__name__,age):
        self.__name__=__name__
        self.age=age
    def full(self,last):
        self.last=last
        return self.__name__,self.last
    def shor(self):
        return self.__name__[0]

obj=Cal('ram',23)
print(obj.full('sharma'))

print(obj.shor())
print(obj.__name__)

print(obj.Cal.__name__)




