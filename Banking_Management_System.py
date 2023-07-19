class Bank:
    def __init__(self):
        self.name = {}
        self.accounts = {}
        self.l_enable = True
        self.established = {}
        self.b_balance = 0
        self.license = {}
        self.accounts = {}
        self.Tloan_amount = 0


    def login(self, email, password):
        if email in self.accounts and self.accounts[email].password == password:
            return self.accounts[email]
        return 

    def g_account(self, email):
        return self.accounts.get(email)
        
    def c_account(self, email, password):
        a = user(email, password)
        self.accounts[email] = a
        return a

    def deposit(self, email, amount):
        a = self.g_account(email)
        if a:
            a.deposit(amount)
            self.b_balance += amount
            print(f"TK {amount} is deposited to the account {email}.\n")
        else:
            print("Account Invalid!\n")
  
    def transfer(self, s_email, r_email, amount):
        s_account = self.g_account(s_email)
        r_account = self.g_account(r_email)

        if s_account and r_account:
            if s_account.balance >= amount:
                s_account.withdraw(amount)
                r_account.deposit(amount)
                print(f"TK {amount} is transferred from the {s_email} to  {r_email}.\n")
            else:
                print("Balance are not sufficient.")
        else:
            print("Accounts(boths) are not exist.")
          
            

    def withdraw(self, email, amount):
        a = self.g_account(email)
        if a:
            if a.balance >= amount:
                a.withdraw(amount)
                self.b_balance -= amount
                print(f"TK {amount} is withdrawal from the account {email}.\n")
            else:
                print("Balance are not sufficient.\n")
        else:
            print("Account Invalid!\n")

  
    def c_balance(self, email):
        a = self.g_account(email)
        if a:
            return a.balance
        else:
            print("Invalid account credentials.")
            return

    def c_t_history(self, email):
        a = self.g_account(email)
        if a:
            return a.t_history
        else:
            print("Invalid account credentials.")
            return

    def t_loan(self, email):
        a = self.g_account(email)
        if a:
            if self.l_enable:
                loan_amount = a.balance * 2
                a.deposit(loan_amount)
                self.b_balance += loan_amount
                self.Tloan_amount += loan_amount
                print(f"Account {email} take loan TK {loan_amount}.\n")
            else:
                print("Loan feature is disabled.")
        else:
            print("Invalid account credentials.")

class user:
    count_account = 0

    def __init__(self, email, password):
        user.count_account += 1
        self.account_number = user.count_account
        self.email = email
        self.password = password
        self.balance = 0
        self.t_history = []

    def withdraw(self, amount):
        self.balance -= amount
        self.t_history.append(f"Withdrawal: {amount}TK")
        
    def deposit(self, amount):
        self.balance += amount
        self.t_history.append(f"Deposit: {amount}TK")


class Admin:
    def __init__(self, bank, email, password):
        self.bank = bank
        self.email = email
        self.password = password

    def login(self):
        if self.bank.login(self.email, self.password):
            print("Login successful By Admin.\n")
            return True
        else:
            print("Sorry! Login not successful.\n")
            return False

    def c_account(self, email, password):
        return self.bank.c_account(email, password)
        
        
    def c_Tloan_amount(self):
        return self.bank.Tloan_amount

    def check_b_balance(self):
        return self.bank.b_balance



bank = Bank()
admin = Admin(bank, "abc@gmail.com", "1234")


account_number1 = bank.c_account("hello1@gmail.com", "H123")
account_number2 = bank.c_account("hello2@gmail.com", "H456")

user1 = bank.login("hello1@gmail.com", "H123")
user2 = bank.login("hello2@gmail.com", "H456")

bank.deposit("hello1@gmail.com", 5000)
bank.withdraw("hello1@gmail.com", 1400)
bank.transfer("hello1@gmail.com", "hello2@gmail.com", 1000)

balance = bank.c_balance("hello1@gmail.com")
print(f"hello1@gmail.com total balance: {balance}TK\n")

history = bank.c_t_history("hello1@gmail.com")
print(f"hello1@gmail.com account: {history}\n")

bank.t_loan("hello1@gmail.com")


admin.login()
account3 = admin.c_account("hello3@gmail.com", "H789")
print(f"New account created: {account3.email}")

bank.deposit("hello3@gmail.com", 2100)

b_balance = admin.check_b_balance()
print(f"Total Bank balance: {b_balance}")

loan_amount = admin.c_Tloan_amount()
print(f"Total loan amount: {loan_amount}")



