#Calling with special forms
def compound_interest(n, r, A0=1000.0, debug=False):
    '''compute compound interest    
       returns a tuple of
       new value of investment
       the interest earned on the principal
    '''
    if debug:
        print('n =', n)
        print('r =', r)
        print('A0 =', A0)
    value = A0*(1+0.01*r)**n
    interest = value - A0
    return value, interest

P = 2000.00
rate = 4.75
term = 15
amount, interest = compound_interest(term, rate, P, True)
print('A = ',round(amount,2))
print('I = ',round(interest,2))

print('After %d intervals, the value is $%.2f, amounting to $%.2f in interest.' 
      % (term, amount, interest))

#Tuple Expansion
invest_tuple = (term, rate, P)
amount, interest = compound_interest(*invest_tuple)
print('After %d intervals, the value is $%.2f, amounting to $%.2f in interest.' 
      % (term, amount, interest))

#Lists 
invest_list = [term, rate, P]
amount, interest = compound_interest(*invest_list)
print('After %d intervals, the value is $%.2f, amounting to $%.2f in interest.' 
      % (term, amount, interest))

#Keyword Expansion
invest_dict = {'r':rate, 'A0':P, 'debug':True, 'n':term}
amount, interest = compound_interest(**invest_dict)
print('After %d intervals, the value is $%.2f, amounting to $%.2f in interest.' 
      % (term, amount, interest))

#Variadic Functions
def average(*args):
    if not args:
        return float('nan')
    else:
        return sum(args)/len(args)
print(average())
average(4,5,6,2,3)

def print_items(**kwargs):
    for key, value in kwargs.items():
        print("%s: %s" % (key, value))
print_items(name='Albert', rate=3.8, age=34)

#Scope of assignment
pi = 3.14
def area(r):
    pi = 3.14159
    val = pi * r**2
    return val
print(area(4))
print(pi)

#Modifying global assignments
x = 2
def add5():
    global x
    x = x + 5
add5()
print(x)

#Classes
#attributes: variables or data.
#methods: functions.
class Point2D(object):
    "Class to represent points in a coordinate system."
    style = "Cartesian"    
    def __init__(self, x, y):
        "Create a new Point at x, y."
        self.x = x
        self.y = y
    def move(self, delta_x, delta_y):
        "Moves point by delta_x and delta_y in the x and y direction."
        self.x += delta_x
        self.y += delta_y

#Instances
p1 = Point2D(-1, 0.5)
print(p1.style, p1.x, p1.y)

p2 = Point2D(1, 1)
p2.move(-.5, .5)
print(p2.x, p2.y)

#A BankAccount class
class BankAccount:  
    def __init__(self, account_ID, first_name, last_name, initial_balance):
        self._account_ID = account_ID
        self._first_name = first_name
        self._last_name = last_name
        self._balance = initial_balance  
    def deposit(self, amount):
        '''BankAccount.deposit(amount) increases balance by amount'''
        if amount<=0:
            raise ValueError('Expect positive amount!')
        self._balance += amount   
    def withdraw(self, amount):
        '''BankAccount.withdraw(amount) increases balance by amount'''
        if amount<=0:
            raise ValueError('Expect positive amount!')
        self._balance -= amount    
    def account_status(self):
        out_string = "%s %s\tID: %s\tBalance: $%.2f" % (
                      self._first_name, self._last_name, 
                      self._account_ID, self._balance)
        print(out_string)
    def owner(self):
        return "%s %s" % (self._first_name, self._last_name)

isaac_account = BankAccount('123456789','Isaac','Newton',576.82)
print(isaac_account.owner())
print(isaac_account.account_status())

isaac_account.deposit(675.32)
print(isaac_account.account_status())

isaac_account._balance += 50.0
print(isaac_account.account_status())

isaac_account.deposit(1200)
isaac_account.withdraw(57.13)
print(isaac_account.account_status())

isaac_account.deposit(-123)
print(isaac_account.account_status())

#Class hierarchies

# Class Mammal is a subclass of class object
class Mammal(object):
    def __init__(self, name):
        self.name = name
        self.legs = 4        
    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.name)        
    def say(self):
        raise NotImplemented

# Class Pet is a subclass of class Mammal
class Pet(Mammal):
    pass

# Class Dog is a subclass of class Pet
class Dog(Pet):
    def say(self):
        print("Woof! My name is %s" % self.name)

# Class Cat is a subclass of class Pet
class Cat(Pet):
    def say(self):
        print("Meow! My name is %s" % self.name)

# Class Bird is a subclass of class object
class Bird(object):
    def __init__(self, name):
        self.name = name
        self.legs = 2        
    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.name)        
    def say(self):
        raise NotImplemented
        
# Class Duck is a subclass of class Bird
class Duck(Bird):
    def say(self):
        print("Quack! my name is %s" % self.name)

# Class Pony is a subclass of class Mammal
class Pony(Mammal):
    def say(self, extra=", Bray!"):
        print("Wheee, my name is %s" % self.name, extra)

#Instances
mypony = Pony("Charlie")
print(mypony.say())

doug = Dog("Doug")
doug.legs = 3
print(doug.say())

animals = [Cat('Sally'), Dog('Rover'), Duck('Dolly'), doug, Cat('Kitty'), mypony]
print(animals)

#Printing
class PrettyPoint2D(Point2D):
    def __str__(self):
        return("Point at [%f, %f]" % (self.x, self.y))
    def __repr__(self):
        return("PrettyPoint2D(x={}, y={})".format(self.x, self.y))

p3 = PrettyPoint2D(4, -5)
print(p3)
repr(p3)

#Math
import math

class Special2D(PrettyPoint2D):
    def __sub__(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx*dx + dy*dy)

p1 = Special2D(0, 0)
p2 = Special2D(1, 1)

print(p2.__sub__(p1))
print(p2 - p1)


