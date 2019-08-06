print('Python', 3)

camelot = "On second thought, let's not go to Camelot. It is a silly place."
help(camelot.split)

#Defining functions
def compound_interest_v1(n, r, A0): 
    '''Compute compound interest'''
    print('n =', n)
    print('r =', r)
    print('A0 =', A0)
    return A0*(1+0.01*r)**n
returned_value = compound_interest_v1(2, 4.75, 200.00)
print(round(returned_value,2))

t = 2
rate = 4.75
P = 200.00
returned_value = compound_interest_v1(t, rate, P)
print(round(returned_value,2))

def compound_interest_v2(intervals, rate, principal): 
    '''Compute compound interest'''
    print('n =', intervals)
    print('r =', rate)
    print('A0 =', principal)
    return principal*(1+0.01*rate)**intervals
P = 1000.00 
rate = 5.75 
for t in range(10): 
    value = compound_interest_v2(t, rate, P)
    print('%2d: $%.2f' % (t,value))

#Default arguments 
def compound_interest_v3(intervals, rate, principal, please_print=False): 
    '''Compute compound interest'''
    if please_print:
        print('n =', intervals)
        print('r =', rate)
        print('A0 =', principal)
    return principal*(1+0.01*rate)**intervals
compound_interest_v3(2, 4.75, 1000)
compound_interest_v3(2, 4.75, 1000, True)

P = 1000.00
rate = 5.75
for t in range(11):
    value = compound_interest_v3(t, rate, P)
    print('%2d: $%.2f' % (t, value))

#Returning more than one value
def compound_interest_v4(intervals, rate, principal, debug=False):
    '''Compute compound interest returns a tuple of current value and interest'''
    if debug:
        print('n =', intervals)
        print('r =', rate)
        print('A0 =', principal)        
    current_value = principal*(1+0.01*rate)**intervals
    interest = current_value - principal    
    return current_value, interest
P = 2000.00
rate = 4.75
term = 15
amount, interest = compound_interest_v4(term, rate, P)
print('After {:d} intervals, the value is ${:.2f}, amounting to ${:.2f} in interest.'.format(term, amount, interest))

f = lambda x,y: x+2*y
print(f(3,4))

#The input function
my_string = input('Please enter a string: ')
print('You entered: %s' % my_string)

