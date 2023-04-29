''''
parent: USer
 - can show user details

child: Bank

 - account balance
 - amount of money
 - can deposit, withdraw, view_balance
'''


class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def ShowAll(self):
        print("Account Details")
        print("Name", self.name)
        print("Age", self.age)
        print("Gender", self.gender)



class TheBank(User):
    def __init__(self,name,age,gender,password):
        super().__init__(name,age,gender)
        self.balance = 0
        self.password = password

    def deposit(self,amount):
        print(self.password)
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Your New Balance is: $",self.balance)

    def withdraw(self,amount):
        self.amount = amount
        if(self.amount > self.balance):
            print("This will overdraft your account")
        else:
            self.balance = self.balance - self.amount
            print("Your New Balance is: $",self.balance)


x = 1

Chris = TheBank('Chris', 27, 'Male','password')

# print((Chris.password)) used to test feature
'''
Features to be added: Username and pass word auth
    - make user and password verification a part of main bank class.
    - have main loop reference the instance and get the instantiation. 
'''
def bankAction():
    choice = 0
    choice = int(input("1 for deposit, 2 for withdraw"))

    if (choice == 1):

        amt = int(input("What is your deposit?"))
        Chris.deposit(amt)

    elif (choice == 2):

        amt = int(input("What is your withdraw?"))
        Chris.withdraw(amt)

    x = int(input("Exit? Enter any number but 1"))

while (x == 1):
    password = input("please input your password:")

    if password == Chris.password:
        bankAction()

    else:
        print("incorrect password")
        password = input("please input your password:")