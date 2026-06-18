import uuid
class Person:
    def __init__(self, first_name: str, last_name: str, id_number: str | int, phone: str, email: str) -> None:
          self.first_name = first_name
          self.last_name = last_name
          self.id_number = id_number
          self.phone = phone
          self.email = email

class bank:
     def __init__(self):
          self.__account = {}
          self.__customers = {}
     def register_customer(self, customer_id: str, person_obj: Person) -> str:
           customer_id = str(uuid.uuid4())
           self.__customers[customer_id] = {
            "first_name": person_obj.first_name,
            "last name" : person_obj.last_name,
            "id number" : person_obj.phone,
            "email" :     person_obj.email
           }
           return person_obj
          
     def create_acc(self):
          pass
     def get_acc(self):
          pass
          






    
class Customer(Person):
    def __init__(self, first_name: str, last_name: str, id_number: str | int, phone: str, email: str, customer_id: int)-> None:
         super().__init__(first_name, last_name, id_number, phone, email)
         self.__customer_id = customer_id
    def get_profile_summary(self):
         pass
    def get_total_balance(self):
         pass
    def verify_identity():
         pass
    
         
class Bank_Account:
    def __init__(self, account_number: int, balance: float, customer_obj: Customer, date_opened: str) -> None:
        self.account_number = account_number
        self.__balance = float(balance)  
        self.__owner = customer_obj  
        self.date_opened = date_opened
        self.__is_active = True 


 