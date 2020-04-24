# Let's review special methods
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

    def __repr__(self):
        pass

    def __str__(self):
        pass


emp_1 = Employee('Aaron', 'Glenn', 100)
emp_2 = Employee('Test', 'User', 200)
