#############-------->  Single Level Inheritance:-
# class Phone: 
#     def __init__(self,price,brand,camera):
#         self.__price=price 
#         self.brand=brand 
#         self.camera=camera 
    
#     def buy(self):
#         print('Buying A Phone')

# class SmartPhone(Phone):
#     pass 
# SmartPhone(1000,'Iphone',3).buy()

#############-------->  MultiLevel Inheritance:-
# class Product:
#     def review(self):
#         print('Product Customer review')
    
# class Phone(Product):
#     def __init__(self,price,brand,camera):
#         self.__price=price    
#         self.brand=brand
#         self.camera=camera 
#     def buy(self):
#         print('Buying A phone')
        
# class SmartPhone(Phone):
#     pass 
# s=SmartPhone(2000,'zoom',23)
# s.buy()
# s.review()
# print(s.brand)

#############-------->  Hierarchical Inheritance:-
# class Phone:
#     def __init__(self,price,brand,camera):
#         self.__price=price 
#         self.brand=brand 
#         self.camera=camera 
#     def buy(self):
#         print('Karidd lo bey!')
        
# class SmartPhone(Phone):
#     pass 
# class FeaturePhone(Phone):
#     pass 

# SmartPhone(2,'Apple',2).buy()

#############-------->  Multiple Inheritance
# class Phone:
#     def __init__(self,price,brand,camera):
#         self.__price=price 
#         self.brand=brand 
#         self.camera=camera
        
#     def buy(self):
#         print("Buying A Product")
        
# class Product:
#     def review(self):
#         print('Customer Review')
    
# class SmartPhone(Phone,Product):
#     pass
# s=SmartPhone(200,'Apple',3)
# s.buy()
# s.review()

#############--------> MRO Example #method resoltion Order
# class Phone:
#     def __init__(self,price,brand,camera):
#         self.price=price 
#         self.brand=brand
#         self.camera=camera
    
#     def buy(self):
#         print("Buying A Phone")
# class Product:
#     def buy(self):
#         print("Product Buy Method")

# class SmartPhone(Product,Phone): # change Product by Phone and vice versa
#     pass
# s=SmartPhone(200,'Apple',5)
# s.buy()

# #############--------> Examples:
# class A:
#     def m1(self):
#         return 20
    
# class B(A):    
#     def m1(self):
#         return 30
#     def m2(self):
#         return 40 
# class C(B):
#     def m2(self):
#         return 20
# obj1=A()
# obj2=B()
# obj3=C()
# print(obj1.m1()+obj3.m1()+obj3.m2())

# #############--------> Examples:
# class A:
#     def m1(self):
#         return 20 
    
# class B(A):
#     def m1(self):
#         val=super().m1+30
#         return val 
# class C(B):
#     def m1(self):
#         val=self.m1()+20 #super is used!!
#         return val 
    
# obj1=C()
# print(obj1.m1())