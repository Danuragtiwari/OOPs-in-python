# Aggregations Demo
class Customer:
    def __init__(self,name,gender,address):
        self.name=name 
        self.gender=gender 
        self.address=address 
    
    def edit_profile(self,new_name,new_city,new_pin,new_state):
        self.name=new_name 
        self.address.change_address(new_city,new_pin,new_state)
    
class Address:
    def __init__(self,city,pincode,state):
        self.city=city
        self.pincode=pincode 
        self.state=state 
    def change_address(self,new_city,new_pin,new_state):
        self.city=new_city 
        self.pincode=new_pin 
        self.state=new_state 
        
        
        
add=Address('pratappur',497223,'CG')
cust=Customer('anu','male',add)
cust.edit_profile('anu','Gurugarm',123456,'haryana')
print(cust.address.city)