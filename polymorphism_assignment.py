
#Parent Class called User
class User():
    name = "Nick"
    email = "npranno@gmail.com"
    password = "123456789"

    def login(self):
        ask_name = input("What is your name? ")
        ask_email = input("What is your email? ")
        ask_pass = input("What is your password? ")
        if (ask_email == self.email and ask_pass == self.password):
            print("Welcome back, {}".format(ask_name))
        else:
            print("The email or password you entered is incorrect.")

#Child Class called Employee
class Employee(User):
    salary = 50,000
    department = "Human Resources"
    pin = "1234"

    def login(self):
        ask_name = input("What is your name? ")
        ask_email = input("What is your email? ")
        ask_pin = input("What is your PIN? ")
        if (ask_email == self.email and ask_pin == self.pin): #asks for pin instead of password
            print("Welcome back, {}".format(ask_name))
        else:
            print("The email or PIN you entered is incorrect.")

#Child Class called Customer
class Customer(User):
    cust_id = "5678"
    cust_location = "Oregon"
    password = "12345678"

    def login(self):
        ask_name = input("What is your name? ")
        ask_id = input("What is your Customer ID? ")
        ask_location = input("What is your Location? ")
        if (ask_id == self.cust_id and ask_location == self.cust_location):
            print("Welcome back, {}".format(ask_name))
        else:
            print("The email or password you entered is incorrect.")






if __name__ == "__main__":
    customer = Customer()
    customer.login()

    emp = Employee()
    emp.login()

