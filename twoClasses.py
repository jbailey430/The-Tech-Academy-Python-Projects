

class user:
    name = 'No Name Provided'
    email = ''
    password = '1qaz2wsx'
    account_number = 0


class Employee(user):
    base_pay = 13.00
    department = 'General'

class Customer(user):
    mailing_address = ''
    mailing_list = True
