from enum import Enum

class AccountType(Enum):
    SAVINGS = "AHORROS"
    CHECKING = "CORRIENTE"

class BankAccount:
    def __init__(self, owner_first_name, owner_last_name, account_number, account_type):
        self.owner_first_name = owner_first_name
        self.owner_last_name = owner_last_name
        self.account_number = account_number
        self.account_type = account_type
        self.balance = 0
    
    def print_info(self):
        print(f"Nombres del titular = {self.owner_first_name}")
        print(f"Apellidos del titular = {self.owner_last_name}")
        print(f"Número de cuenta = {self.account_number}")
        print(f"Tipo de cuenta = {self.account_type.value}")
        print(f"Saldo = {self.balance}")
    
    def check_balance(self):
        print(f"El saldo actual es = {self.balance}")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f"Se ha consignado ${amount} en la cuenta. El nuevo saldo es ${self.balance}")
            return True
        else:
            print("El valor a consignar debe ser mayor que cero.")
            return False
    
    def withdraw(self, amount):
        if (amount > 0) and (amount <= self.balance):
            self.balance = self.balance - amount
            print(f"Se ha retirado ${amount} en la cuenta. El nuevo saldo es ${self.balance}")
            return True
        else:
            print("El valor a retirar debe ser menor que el saldo actual.")
            return False
    
    def compare_accounts(self, account):
        if self.balance >= account.balance:
            print("El saldo de la cuenta actual es mayor o igual al saldo de la cuenta pasada como parámetro.")
        else:
            print("El saldo de la cuenta actual es menor al saldo de la cuenta pasada como parámetro.")
    
    def transfer(self, account, amount):
        if self.withdraw(amount):
            account.deposit(amount)


account1 = BankAccount("Pedro", "Pérez", 123456789, AccountType.SAVINGS)
account2 = BankAccount("Pablo", "Pinzón", 44556677, AccountType.SAVINGS)
account1.deposit(200000)
account2.deposit(100000)
account1.compare_accounts(account2)
account1.transfer(account2, 50000)
account1.check_balance()
account2.check_balance()