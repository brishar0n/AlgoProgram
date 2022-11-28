from Account import Account
from Customer import Customer
from Bank import Bank

class ATM: 
    # Conduct def init in order for ATM system to allow user to input their information
    def __init__(self, data):                           
        self.__data = data

        self.__userIndex = None
        
        self.__bank = Bank("Bri's ATM")           
        for index, data in enumerate(self.__data):
            self.__bank.addCustomer(data['firstName'], data['surname'], data['pin'])       
            self.__bank.getCustomers(index).setAccount(Account(data['balance']))     

        self.__mainMenu()

    # Moving on to the menu of the ATM system:
    def __mainMenu(self):           
        notExit = True
        while notExit:                        # Different result depending whenn you are a administrator or customer
            try:
                print(" ")
                print("Welcome to Bri's Bank (^-^*)/")
                print(" ")
                print("Please choose your role: ")
                print("1. Administrator")
                print("2. Customer")
                print("3. Exit")
                choice = int(input("\nChoose your option: "))
                notExit = self.__runMainMenu(choice)
            except:
                print("Please enter one of the options mentioned.")

    def __runMainMenu(self,choice):
        notExit = True
        while notExit: 
            if choice == 1:
                if self.__adminAuthentication() == True:        # Confirmation of Admin
                    self.__administratorMenu()                  # If confirmation is a success, it'll take the user to the admin menu
                return True
            elif choice == 2:
                if self.__customerAuthentication() == True:     # Confirmation of Customer
                    self.__customerMenu()                       # If confirmation is a success, it'll take the user to the customer menu
                return True
            elif choice == 3: 
                notExit = False         
                print("Thank you for trusting Bri's ATM! Come back anytime!")
                return False           
    

# ADMINISTRATOR
    def __adminAuthentication(self):         
        adminPin = input("Enter your Pin : ")
        while not self.__adminPin(adminPin):
            print("Incorrect pin input, try again.")
            adminPin = input("Enter your Pin: ")

    def __adminPin(self,adminPin):       
        if adminPin == "1117":
            self.__administratorMenu()          
            return True

        return False

    def __administratorMenu(self):               
        notExit = True
        while notExit: 
            try:
                print("")
                print("What would you like to do?")
                print("1. Add Customer")
                print("2. Delete Customer")
                print("3. Edit Customer")
                print("4. Search Customer")
                print("5. Exit")
                print(" ")
                option = int(input("Choose your option: "))
                notExit = self.__runadministratorMenu(option)
            except ValueError:
                print("Please enter a valid option.")

    def __runadministratorMenu(self, option):
        # Option 1 - Add Customer
        loop = 1
        while loop == 1:
            if option == 1:                
                firstName = input("First Name: ")
                surname = input("Surname: ")
                pin = input("Pin: ")
                balance = input("Balance: ")

                self.__data.append(
                    {
                        'firstName': firstName,
                        'surname': surname,
                        'pin' : pin,
                        'balance': int(balance)
                    }
                )

                self.__bank.addCustomer(firstName, surname, pin)      
                self.__bank.getCustomers(len(self.__data)-1).setAccount(Account(int(balance)))     
                return True

            # Option 2 - Delete customer
            elif option == 2:                 
                delete = int(input("\nWhich customer index do you want to delete?: "))

                del self.__data[int(delete)]

                print("Cusomter data successfully deleted.")
                return True

            # Option 3 - Edit customer
            elif option == 3:               
                edit = int(input("Which customer index do you want to edit?: "))

                if edit > len(self.__data):
                    print(f"There are only {len(self.__data)} customers. Please enter a proper value!")
                else:
                    firstName = input("First Name: ")
                    surname = input("Surname: ")
                    pin = int(input("Pin : "))
                    balance = int(input("Balance: "))

                    self.__data[edit-1] = {
                        'firstName': firstName,
                        'surname': surname,
                        'pin': pin,
                        'balance': balance
                    }

                return True

            # Option 4 - Search customer
            elif option == 4:                 
                for index, data in enumerate(self.__data):
                    print(f"""
Customer ID - {index}:
    > First Name: {data["firstName"]}
    > Surname: {data["surname"]}
    > Customer Pin: {data["pin"]}
    > Balance: {data["balance"]}
                        """)
                return True

            # Option 5 - Exit
            elif option == 5:                  
                loop = 0 
                print("Now returning to the start menu ...")
                return False
    
# CUSTOMER
    def __customerAuthentication(self):           
        credFirstName = input("First Name: ")
        credSurname = input("Surname: ")
        credPin = input("Pin : ")

        while not self.__checkCredentiasurnames(credFirstName, credSurname, credPin):    
            print("Incorrect credential input, please re-enter your credential.")
            credFirstName = input("First Name: ")
            credSurname = input("Surname: ")
            credPin = input("Pin: ")
        return True             

    def __checkCredentiasurnames(self, firstName, surname, pin):
        for index, data in enumerate(self.__data):
            if firstName == data['firstName'] and surname == data['surname'] and pin == data['pin']:
                self.__userIndex = index
                return True
        return False

    def __customerMenu(self):
        notExit = True
        while notExit: 
            try: 
                print(" ")
                print("Please choose one of the following options:")
                print("1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Log out")
                option = int(input("Choose your option: "))
                notExit = self.__runCustomerMenu(option)
            except: 
                print("Please enter a valid option.")

    def __runCustomerMenu(self, option):
        loop = 1
        while loop == 1:
            while option not in range(1,5):
                print("Your option is invalid, please re-enter your choice.")
                option = int(input("Choose your option: "))
            # Option 1 - Check balance
            if option == 1:           
                self.__bank.getCustomers(self.__userIndex).getAccount().checkBalance()
                return True
            
            # Option 2 - Deposit
            elif option == 2:
                amount = int(input("How much would you like to deposit?: "))
                self.__bank.getCustomers(self.__userIndex).getAccount().deposit(amount)
                return True

            # Option 3 - Withdraw
            elif option == 3:       
                amount = int(input("How much would you like to withdraw?: "))
                self.__bank.getCustomers(self.__userIndex).getAccount().withdraw(amount)
                return True

            # Option 4 - Log out
            elif option == 4:
                loop = 0
                print("Thank you for using Bri's ATM! Come back anytime!")
                return False