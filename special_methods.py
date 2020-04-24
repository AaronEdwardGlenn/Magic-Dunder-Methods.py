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
        pass

    def __str__(self):
        pass


emp_1 = Employee('Aaron', 'Glenn', 100)
emp_2 = Employee('Test', 'User', 200)

print(1+2)
print('a'+'b')

# this doesn't print out anything useful. our special methods are going to change this.
print(emp_1)

repr(emp_1)  # repr is info on an object for devlopers
str(emp_1)  # str is info that will be displayed for users and stuff
