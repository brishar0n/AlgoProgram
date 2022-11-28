class Customer:
    def __init__(self,f,l):
        self.__fName = f
        self.__lName = l
        
    def getFirstName(self):
        return self.__fName
    
    def getLastName(self):
        return self.__lName
    
    def getAccount(self):
        return self.__account
    
    def setAccount(self,account):
        self.__account = account