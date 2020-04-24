# Let's review special methods(magic methods)
# These allow us to emulate some of the built in behavior in python. it's also how we impliment operator overloading.
# the __ double underscores that we find everywhere in python are called dunders.


class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return('{}, {}'.format(self.first, self.last))

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    def __repr__(self):  # this is needed when we have the str that follows this. otherwise it will just default to repr. having it as pass is all that is needed
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Aaron', 'Glenn', 100)
emp_2 = Employee('Test', 'User', 200)

# this doesn't print out anything useful. our special methods are going to change this.

print(repr(emp_1))
print(str(emp_1))


repr(emp_1)  # repr is info on an object for devlopers
str(emp_1)  # str is info that will be displayed for end users and stuff

print(emp_1 + emp_2)

# NOTE review python docs to see math dunders

print('test'.__len__())

print(len(emp_1))
