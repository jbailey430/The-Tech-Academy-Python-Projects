

#Parent Class User
class User:
    name = "Steve"
    email = "Steve@gmail.com"
    password = "12345678"

def getLogin(self):
    entry_name =("Enter your name: ")
    entry_email = input("Enter your email: ")
    entry_password = input("Enter your password: ")
    if (entry_email == self.email and entry_password == self.password):
        print("Welcome back, {}!".format(entry_name))
    else:
        print("The password or email is incorrect.")

#Child Class Employee
class Employee(User):
    base_pay = 12.00
    department = "General"
    pin_number = 3091

def getLogin(self):
    entry_name =("Enter your name: ")
    entry_email = input("Enter your email: ")
    entry_pin = input("Enter your pin: ")
    if (entry_email == self.email and entry_pin == self.pin):
        print("Welcome back, {}!".format(entry_name))
    else:
        print("The pin or email is incorrect.")

#not sure if I need the if __name__ == "__main__:" here or not?
customer = User()
customer.getLogin()

manager = Employee()
manager.getLogin()
