class Atm:
    # static/class variables
    counter=1
   
    # function or method
    def __init__(self): #init is a Constructor,it is special method,in which it execute automatically when object of that class is created.
        
        self.pin=''
        self.balance=0
        self.sno=Atm.counter # to access static variable ,we use class name as shown here!!
        Atm.counter+=1 
        self.menu()
    @staticmethod
    def get_counter():
        return Atm.counter 
    @staticmethod # it is used to express that static method is used here!
    def set_counter(new):
        if type(new)==int:
            Atm.counter=new 
        else:
            print('Not Allowed!')
    def menu(self):
        user_input=input(""" Hello,How would you like to proceed?
                         1.Enter 1 to create Pin
                         2.Enter 2 to Deposit
                         3.Enter 3 to Withdraw 
                         4.Enter 4 to check Balance
                         5.Enter 5 to Exit
                         """)
        if user_input=='1':
            self.create_pin()
            print('Create Pin')
        elif user_input=='2':
            self.deposit()
            print('Deposit')
        elif user_input=='3':
            self.withdraw()
            print('WithDraw')
        elif user_input=='4':
            self.check_balance()
            print('Check Balance')
        else:
            print('Exit')
    def create_pin(self):
        self.pin=input('Enter Your Pin')
        
        print('Pin set Successfully')
        self.menu()
    def deposit(self):
        temp=input('Enter your Pin')
        if temp==self.pin:
            amt=int(input('Enter Amount'))
            self.deposit+=amt 
            print('Deposit Successfully!')
        else:
            print('''Wrong Pin
                Try later ;(''')
        self.menu()
    def withdraw(self):
        temp=input('Enter your Pin')
        if temp==self.pin: 
            amt=int(input('Enter money to be withdraw'))
            if amt<self.balance:
                self.balance-=amt  
            else:
                print('Insufficient funds ')
        else:
            print('Invalid Pin')     
        self.menu()
    def check_balance(self):
        temp=input('Enter your Pin')
        if temp==self.pin:
            print(self.balance )
        else:
            print('Invalid Pin')
        self.menu()
         
        
g=Atm()

        
