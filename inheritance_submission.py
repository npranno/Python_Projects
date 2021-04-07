

class User:
    name = 'No Name Given'
    email = ''
    password = "password1234'
    user_id = '0'

class Teacher(User):
    salary = '50,000'
    classif = 'instructor'

class Student(User):
    gpa = '3.5'
    address = '1234 First St'
