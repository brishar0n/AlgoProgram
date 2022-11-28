from Customer import Customer

class Bank:
    def __init__(self,bName):
        self.__bName = bName
        self.__numOfCust = 0
        self.__customers = list()
        
    def addCustomer(self,f,l):
        self.__customers.append(Customer(f,l))
        self.__numOfCust += 1
        
    def getNumOfCust(self):
        return self.__numOfCust
    
    def getCustomer(self,index):
        return self.__customers[index]
    