#Python developers use a few basic numeric data types to build complex programs.
#int integer type 
#float floating-point type 
#complex complex (floating-point) type 

#Binary mathematical operators in Python behave in a straightforward way as with most programming languages.
#+ addition
#- subtraction
#* multiplication
#/ division
#// floor division
#** exponentiation
#% remainder

a=15-7
b=13.2+4.7
c=3/4
d=3//4
e=5%3

print(type(a))
print(type(b))

#The retail price of a bicycle tire is $54.99 but the bicycle store gets a 20% discount. 
#Shipping costs $4.95 each for the first 5 tires and $2.25 for each additional one. 
#What is the total wholesale cost for a bicycle store to order 50 tires?
quantity = 50
base_price = quantity * 54.99
discount = base_price * 0.20
shipping_cost = 5*4.95 + (quantity-5)*2.25
total_cost = base_price - discount + shipping_cost
print(total_cost)

#Suppose you drive 69.1 kilometres in 1 hour, 13 minutes, and 23 seconds. 
#What is your average speed in miles per hour? 
#Remember, there are 1.61 kilometres in a mile.
d=69.1/1.61
t=1 + (13/60) + (23/3600)
MPH=round(d/t,2)
print(MPH)

#For each of the following expressions, predict the value & type of the expression.
price_per_unit = 5.65
quantity = 12
price = price_per_unit * quantity
print(type(quantity/4))
print(type(quantity//4))
print(type(quantity//4.0))
print(type(price * 0.07))
print(type(3 + 2 * quantity))

balance = 100
interest_rate = 5
interest = (interest_rate/100) * balance
balance += interest
print(balance)

my_string1 = 'string'
print(my_string1)
my_string2 = "string"
print(my_string2)
my_string3 = '''a
string
with
multiple
lines'''
print(my_string3)
my_string4 = 'an "embedded" quote'
print(my_string4)
my_string5 = '42'
print(type(my_string5))

a = 'Polar'
b = 'Bear'
space = ' '
print(a + space + b)
print(5 * 'And')

a_number = '42'
print(int(a_number))
print(float(a_number))

#Use the method count to determine the number of times the letter 'a' occurs in 'abracadabra'.
Word = 'abracadabra'
print(Word.count ('a'))

#Use the method replace to substitute the suffix 'pdf' for 'txt' in the string 'filename.txt'.
filename = 'filename.txt'
print(filename.replace('txt', 'pdf'))

b = 2
a = 2.7
string = 'Python'
print(string, b, a)

unformatted = 'The value of 2/3 is {}'
print(unformatted.format(2/3))

trimmed = 'The value of (12 + 2/3) is {:.3f}, and {:.2f}'
print(trimmed.format(12 + 2/3, 42))

#Construct a sequence of formatted strings using strings & the .format method to display the value 5/7 with varying precision as follows:
#The value of 5/7 to 3 decimal places is 0.714.
#The value of 5/7 to 4 decimal places is 0.7143.
#The value of 5/7 to 5 decimal places is 0.71429.
#The value of 5/7 to 6 decimal places is 0.714286.
#The value of 5/7 to 7 decimal places is 0.7142857.
print('The value of 5/7 to 3 decimal places is {:.3f}'.format(5/7))
print('The value of 5/7 to 4 decimal places is {:.4f}'.format(5/7))
print('The value of 5/7 to 5 decimal places is {:.5f}'.format(5/7))
print('The value of 5/7 to 6 decimal places is {:.6f}'.format(5/7))
print('The value of 5/7 to 7 decimal places is {:.7f}'.format(5/7))

import math
print(type(math))

print('The square root of 2 is', math.sqrt(2))
print('The value of pi is,', math.pi)

# the numpy.sqrt function can be applied to lists/arrays elementwise
import numpy as np
print(np.sqrt([1,2,3]))

from math import pi as PI
print(PI)

import math
def radians_to_degrees(radian):
    return 360*radian/2./math.pi
print(radians_to_degrees(2))

from numpy import mean
numbers = [1, 2, 8, 10, 2, 4]
print(mean(numbers))

import numpy as np
numbers = [1, 2, 8, 10, 2, 4]
print(np.mean(numbers))

from scipy.stats import describe
numbers = [0, 1, 1, 2, 3 ,5]
print(describe(numbers))

from scipy import stats
numbers = [0, 1, 1, 2, 3 ,5]
print(stats.describe(numbers))

print(help(math.sqrt))

