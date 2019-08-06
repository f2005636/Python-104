is_true = True
print(type(is_true))
print(not is_true)

#Standard comparisons between numbers follow fairly standard conventions.
#less than < 
#greater than > 
#less than or equal to <=
#greater than or equal to >= 
#equal to ==
#not equal to != 

thing = 3/4 > 0.5
print(thing)

#For each of the following comparisons, predict the resulting value.
print(1 > 2)
print(3.4 <= 9.5)
print(2 == (5-3))
print((1/7 + 4/7)  == 5/7)

print(2 == 2.0)
print(3.141596 < 3)

#Comparison operators may also be chained together to compare more than two values. 
#Read these chained comparisons in the natural way, left-to-right.
print(1 + 1 == 2.0 == 3 - 1)
print(1 + 1 == 2.0 and 2.0 == 3 - 1)

#Values can be combined logically using or, and, or not.
#disjunction - or
#conjunction - and
#negation - not
value = 42
is_odd = value % 2 != 0
is_even = value % 2 == 0
print(is_odd or is_even)
print(is_odd and is_even)

print('hello' == "Hello")

letters = 'My hovercraft is full of eels.'
print('e' in letters)
print('full' in letters)

#Empty objects are considered to be False
empty = ''
t = bool(empty)
print(t)

filled = 'False'
t = bool(filled)
print(t)

#The numbers 0 is False, all else are True
number = 0
n = bool(number)
print(n)

number = -1.0
n = bool(number)
print(n)

#Branching: if-elif-else constructs
import random
profit = random.randint(-5,5)
yes = profit >= 0
if yes:
    print("Positive profit of ${}! Yay, we're in the black!".format(profit))
else:
    print("Negative profit of ${}! Oh no, we're in the red!".format(profit))
print("Accounts reviewed, let's go home...")

#The ternary if-else operator
profit = random.randint(-5, 5)
my_bonus = 1000.00 if profit>0 else 0.00
print('Profit = ${}'.format(profit))
print('Bonus  = ${}'.format(my_bonus))

#When using the while construct, the generic format is
#while condition:
#    do something
#where condition is a boolean-valued expression (e.g., term<10 above). 
#The body of the loop repeats until the value condition is False 
#or until a break statement executes inside the loop body.
total = 0
term = 0
while term < 10:
    term += 1
    total += term
print('The total is', total)

#When using the for construction Python, the generic format is
#for item in collection:
#    do_something(item)
#The inputs to range are:
#start: initial value [optional; defaults to 0]
#stop: the final value plus 1 [required]
#step: the amount to increment between start and stop-1 [optional; defaults to 1]
#Examples:
#range(10) produces the values 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.
#range(1,11,2) produces the values 1, 3, 5, 7, 9.
total = 0
for term in range(1,11):
    total += term
print('The total is', total)

#It is common to nest branching (if-elif-else) within a loop (for or while) 
#to selectively carry out different operations depending on some condition.
#1.Runs 100,000 total_iterations.
#2.Rolls the dice every iteration.
#3.If the value is 2 increments a counter number_of_twos.
#4.Prints the probability of rolling 2 as number_of_twos / total_iterations * 100 .
total_iterations = 100000
term = 0
total = 0
number_of_twos = 0
while term < total_iterations:
    roll = random.randint(1,6)
    if roll == 2:
        number_of_twos += 1
    term += 1
    total += term
print(number_of_twos / total_iterations * 100)
print('The total is', total)

#continue keyword - To skip to the next iteration, we use the continue keyword.
weekly_profits = [15441.78, -4995.9, 17612.35, -1699.89, 13508.56, 8197.6, 2129.29, -7164.04]
for profit in weekly_profits:
    if profit < 0:
        continue
    print('Profit:', profit)

for profit in weekly_profits:
    if profit > 0:
        print('Profit:', profit)
        
#break keyword - We can use break to completely stop a loop.
for profit in weekly_profits:
    if profit < 0:
        break
    print('Profit:', profit)
        
#Exception
line = "I didn't expect the Spanish Inquisition."
try:
    line.say()
except:
    print('No one expects the Spanish Inquisition!')

#Catch ZeroDivisionError and continue to the next value.
#Catch ValueError and print 'The value is imaginary'.
import math
for i in range(10):
    try:
        number = random.randint(-10, 10)
        print(math.sqrt(1/number))
    except ZeroDivisionError:
        continue
    except ValueError:
        print("The square root of 1/{} is imaginary".format(number))

    
    