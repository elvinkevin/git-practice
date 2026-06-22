# import uuid
# class Person:
#     def __init__(self, first_name: str, last_name: str, id_number: str | int, phone: str, email: str) -> None:
#           self.first_name = first_name
#           self.last_name = last_name
#           self.id_number = id_number
#           self.phone = phone
#           self.email = email

# class bank:
#      def __init__(self):
#           self.__account = {}
#           self.__customers = {}
#      def register_customer(self, customer_id: str, person_obj: Person) -> str:
#            customer_id = str(uuid.uuid4())
#            self.__customers[customer_id] = {
#             "first_name": person_obj.first_name,
#             "last name" : person_obj.last_name,
#             "id number" : person_obj.id_number,
#             "phone" : person_obj.phone,
#             "email" :     person_obj.email
#            }
#            return person_obj
          
#      def create_acc(self):
#           pass
#      def get_acc(self):
#           pass
           
# class Customer(Person):
#     def __init__(self, first_name: str, last_name: str, id_number: str | int, phone: str, email: str, customer_id: int)-> None:
#          super().__init__(first_name, last_name, id_number, phone, email)
#          self.__customer_id = customer_id
#     def get_profile_summary(self):
#          pass
#     def get_total_balance(self):
#          pass
#     def verify_identity():
#          pass
    
         
# class Bank_Account:
#     def __init__(self, account_number: int, balance: float, customer_obj: Customer, date_opened: str) -> None:
#         self.account_number = account_number
#         self.__balance = float(balance)  
#         self.__owner = customer_obj  
#         self.date_opened = date_opened
#         self.__is_active = True 

import uuid

class Person:
    def __init__(self, first_name: str, last_name: str, id_number: str | int, phone: str, email: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        self.phone = phone
        self.email = email

class Customer(Person):
    def __init__(self, first_name: str, last_name: str, id_number: str | int, phone: str, email: str, customer_id: str) -> None:
        super().__init__(first_name, last_name, id_number, phone, email)
        self.__customer_id = customer_id
        self.__accounts = [] # Keeps track of this customer's accounts

    def get_customer_id(self) -> str:
        return self.__customer_id

    def add_account(self, account_obj) -> None:
        self.__accounts.append(account_obj)

    def get_profile_summary(self) -> str:
        return f"Customer {self.__customer_id}: {self.first_name} {self.last_name}"

    def get_total_balance(self) -> float:
        return sum(acc.get_balance() for acc in self.__accounts)
         
    def verify_identity(self, provided_id: str | int) -> bool:
        return str(self.id_number) == str(provided_id)

class Bank_Account:
    def __init__(self, account_number: str, balance: float, customer_obj: Customer, date_opened: str) -> None:
        self.account_number = account_number
        self.__balance = float(balance)  
        self.__owner = customer_obj  
        self.date_opened = date_opened
        self.__is_active = True

    def get_balance(self) -> float:
        return self.__balance

class Bank: # Capitalized for standard naming conventions
    def __init__(self) -> None:
        self.__accounts = {}   # Maps account_number -> Bank_Account object
        self.__customers = {}  # Maps customer_id -> Customer object
     
    def register_customer(self, person_obj: Person) -> Customer:
        # Generate ID, create Customer object, and store the object directly
        generated_id = str(uuid.uuid4())[:8] # Shortened for readability
        new_customer = Customer(
            first_name=person_obj.first_name,
            last_name=person_obj.last_name,
            id_number=person_obj.id_number,
            phone=person_obj.phone,
            email=person_obj.email,
            customer_id=generated_id
        )
        self.__customers[generated_id] = new_customer
        return new_customer
          
    def create_acc(self, customer_obj: Customer, initial_deposit: float, date_str: str) -> Bank_Account:
        acc_num = str(uuid.uuid4().fields[0]) # Generates a numeric-looking ID
        new_account = Bank_Account(acc_num, initial_deposit, customer_obj, date_str)
        
        # Link account to both the bank registry and the customer object
        self.__accounts[acc_num] = new_account
        customer_obj.add_account(new_account)
        return new_account

    def get_acc(self, account_number: str) -> Bank_Account | None:
        return self.__accounts.get(account_number, None)


 