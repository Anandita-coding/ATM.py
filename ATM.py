class ATM(object):
    def __init__(self):
        self.pin == 1100
        self.pin_entered 
        self.amount
        self.options
        self.balance = 50000
       
    
    
      
   
    def get_pin(self):
        self.pin_entered = int(input("Enter your pin to authenticate"))   
        if self.pin_entered == self.pin:
              self.options = int(input("Press 1 to withdraw cash\n Press 2 for balance enquiry\n"))

       
       
    def transaction_status(self):
        if self.options == 1:
            self.amount = int(input("Enter the amount you wish to withdraw under Rs.10,000"))
            if self.amount<10000:
                print("Your Transaction Was Succesful please Collect Your cash")
            elif self.amount>10000:
                print("Please Enter An Amount Below Rs.10,000")
                self.balance = self.balance - self.amount
        elif self.options == 2:
            print("Your Balance Is ", self.balance)
            
custom = ATM()
custom.get_pin()
custom.transaction_status()