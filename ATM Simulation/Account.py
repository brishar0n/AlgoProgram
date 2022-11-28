class Account:
    def __init__(self,balance):
        self.__balance = balance
        
    def getBalance(self):
        return self.__balance
  
    def deposit(self,amt):
        if amt <= 0:
            return False
        else:
            self.__balance += amt
            return True
    
    def withdraw(self,amt):
        if amt > self.__balance:
            return False
        else:
            self.__balance -= amt
            return True