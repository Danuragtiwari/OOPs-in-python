# class Customer:
#     def __init__(self,name,gender):
#         self.name=name 
#         self.gender=gender 
        
     
# def greet(customer):
#     if customer.gender=='male':
#         print('hello',customer.name,'sir')   
#     else:
#         print('hello',customer.name,"ma'am")
#     cust2=Customer('anu','female')
#     return cust2
# cust=Customer('Anu','male')
# print(cust.name)
# new=greet(cust)
# print(new.name)

# pass by reference:-
# class ke objects are also mutable like list,dict,sets
# class Customer:
#     def __init__(self,name):
#         self.name=name 
    
# def greet(customer):
#     print(id(customer))
#     customer.name='nitish'
#     print(customer.name)
#     print(id(customer))
#     # pass  

# cust=Customer('anu')
# print(id(cust))

# greet(cust)

# print(cust.name)


# collections of objects:-

class Customer:
    def __init__(self,name,age):
        self.name=name 
        self.age=age 
    
    def intro(self):
        print('i am',self.name,'and i am',self.age)
    
c1=Customer('Anu',22)
c2=Customer('anu',23)
c3=Customer('amu',20)

l=[c1,c2,c3] #lists of objects
for i in l:
    i.intro()
