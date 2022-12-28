class Fraction:
      
    def __init__(self,n,d):
        
        self.num=n 
        self.den=d   
        
    def __str__(self): #when the print is executed this function is executed!!
        # return 'helo'
        return '{}/{}'.format(self.num,self.den)
    
    def __add__(self,other): #when x+y is executed then this method is used!!
        temp_num=self.num*other.den+other.num*self.den 
        temp_den=self.den*other.den  
        return '{}/{}'.format(temp_num,temp_den)
    
    def __sub__(self,other): #when x-y is executed then this method is used!!
        temp_num=self.num*other.den-other.num*self.den 
        temp_den=self.den*other.den  
        return '{}/{}'.format(temp_num,temp_den)
    
    def __mul__(self,other): #when x*y is executed then this method is used!!
        temp_num=self.num*other.num
        temp_den=self.den*other.den  
        return '{}/{}'.format(temp_num,temp_den)
    
    def __truediv__(self,other): #when x/y is executed then this method is used!!
        temp_num=self.num*other.den
        temp_den=self.den*other.num 
        return '{}/{}'.format(temp_num,temp_den)
       
x=Fraction(3,4)
y=Fraction(4,3)
print(x+y)
print(x-y)
print(x*y)
print(x/y)