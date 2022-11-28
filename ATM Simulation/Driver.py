from Account import Account
from Customer import Customer
from Bank import Bank
from ATM import ATM
    
if __name__ == "__main__":
    data = [
        {
            "f": "Brigitte",
            "l": "Alexander",
            "customerPin": "2004",
            "balance": 150000
        }
    ]
    ATM(data)