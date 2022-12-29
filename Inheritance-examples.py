# Example:1 Inheriting Constructor
# class Phone:
#     # pass 
#     def __init__(self,price,brand,camera):
#         print('Inside Phone Constructor')
#         self.price=price 
#         self.brand=brand 
#         self.camera=camera  
    
#     def buy(self):
#         print('Buying the Phone')
#     def return_phone(self):
#         print('Returning a phone')

# class FeaturePhone(Phone):
#     pass 
# class SmartPhone(Phone):
#     pass  

# s=SmartPhone(2000,'Apple',13)
# print(s.price)
# s.buy()

# Example:2 Inheriting Private members
# class Phone:
#     def __init__(self,price,brand,camera):
#         self.__price=price 
#         self.brand=brand 
#         self.__camera=camera 
    
#     def buy(self):
#         print('Buying the Phone')
#     def return_phone(self):
#         print('Returning a Phone') 
    
# class FeaturePhone(Phone):
#     pass

# stu=FeaturePhone(2000,'iphone',3)
# print(stu._Phone__price) #to get private data!
# # print(stu.__price) #not have access to private variables
# print(stu.brand)

# Example:3 Method overriding-->Polymorphism:-(method Overriding,Method Overloading,Operator Overloading)

# class Phone:
#     def __init__(self,price,brand,camera):
#         self.__price=price 
#         self.brand=brand 
#         self.camera=camera
#     def buy(self):
#         print('Buying a phone')
    
# class SmartPhone(Phone):
#     def buy(self):
#         print('Buying a smartPhone')
        
# a=SmartPhone(20000,'Iphone',12)
# a.buy()

# Example:4 :-
# class Parent:
#     def __init__(self,num):
#         self.__num=num 
#     def get_num(self):
#         return self.__num 
# class Child(Parent):
#     def show(self):
#        print('This is in Child class')

# son=Child(100)
# print(son.get_num())
# son.show()

# Example:5 
# class Parent:
#     def __init__(self,num):
#         self.__num=num 
#     def get_num(self):
#         return self.__num 
# class Child(Parent):
#     def __init__(self,val,num):
#         self.__val=val 
#     def get_val(self):
#         return self.__val 
# son=Child(100,10)
# print('Parent: Num',son.get_num())
# print('Child: Num ',son.get_val())

# Example:6 
# class A:
#     def __init__(self):
#         self.var1=100 
    
#     def display1(self,var1):
#         print('Class A',self.var1,var1)

# class B(A):
#     def display2(self,var1):
#         print('Class B',self.var1)
        
# obj=B() 
# obj.display1(200)

# Example:7  Super keyword example:-
# class Phone:
#     def __init__(self,price,brand,camera):
#         self.__price=price  
#         self.brand=brand 
#         self.camera =camera  
    
#     def buy(self):
#         print('Buying a Phone')
#     def return_phone(self):
#         print('Returning a phone')
        
# class SmartPhone(Phone):
#     def buy(self):
#         print('Buying a SmartPhone')
#         super().buy()
        
# a=SmartPhone(200,'jio',31)
# a.buy()

# Example:8 On super keyword:-
# class Phone:
#     def __init__(self,price,brand,camera):
#         self.__price=price 
#         self.brand=brand 
#         self.camera=camera  
    
    

# class SmartPhone(Phone):
#     def __init__(self,price,brand,camera,os,ram):
#         super().__init__(price,brand,camera)
#         self.os=os 
#         self.ram=ram 
#         print('Inside SmartPhone')
   
        
# a=SmartPhone(200,'apple',21,'android',32)
# print(a.os)
# print(a._Phone__price) #to get private data


# Example:9 On super keywords:-
# class Parent:
#     def __init__(self,num):
#         self.__num=num 
#     def get_num(self):
#         return self.__num 
# class Child(Parent):
#     def __init__(self,num,val):
#         super().__init__(num)
#         self.__val=val 
    
#     def get_val(self):
#         return self.__val 
# son=Child(100,200)
# print(son.get_num())
# print(son.get_val())

# Example:10 super keywords:-
# class Parent:
#     def __init__(self):
#         self.num=100 

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.var=200 
#     def show(self):
#         print(self.num)
#         print(self.var)

# son=Child()
# son.show()

# Example:11  super keywords:-
# class Parent: 
#     def __init__(self):
#         self.__num=100 
#     def show(self):
#         print('Parent',self.__num)

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.__var=10 
    
#     def show(self):
#         print('Child',self.__var)
# dad=Parent()
# dad.show()
# son=Child()
# son.show() 
