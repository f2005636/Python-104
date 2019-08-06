#Lists
import random
objects = ['a', 0, 2.0, print, random]
print(type(objects))

for thing in objects:
    its_type = type(thing)
    print("{} is an object of type {}".format(thing, its_type))
    
#Adding items
objects.append('Python')
for thing in objects:
    print(thing)

#Length
print(len(objects))

#Concatenation and Arithmetic
new_list = objects + [1,1,2,3,5]
print(new_list)

another_list = [3.1415] * 5
for i in another_list:
    print(i)

another_list = []
another_list.append(42)
another_list.append('string')
print(another_list)

#Indexing
integers = [1, 2, 3, 4, 5]
print(integers[0])
print(integers[2])
print(integers[-1])

#Assignment
integers[2] = 3.1415
print(integers)
integers[-1] *= 10
print(integers)

#Removing items
integers.remove(2)
print(integers)
integers.pop()
print(integers)
integers.pop(1)
print(integers)

#Tuples
the_tuple = (1, 2.0, 'five!')
for thing in the_tuple:
    print(thing)

#Create an empty tuple
empty = ()
print(empty)

#Create a singleton tuple
singleton = 3,
print(singleton)

#Tuple packing & unpacking
#New values cannot be appended.
#Existing values cannot be re-assigned.
#Values cannot be removed.
a='string'
b=2.0
c=42
a_tuple = (a,b,c)
my_string, my_float, my_int = a_tuple
print(my_string)
print(my_float)
print(my_int)

#Swapping values
a,b = b,a
print(a)
print(b)

#Sets
numbers = {3,4,3,2,5,8,9,2,3,4,0}
for n in numbers:
    print(n)

#Adding items
numbers.add(2.0)
numbers.add(7)
numbers.add(2.1)
for n in numbers:
    print(n)

#Arithmetic
users = {'Dave', 'Bob', 'Alice', 'Doug'}
admin = {'Bob', 'Alice', 'Fred'}
print(users | admin)
print(users - admin)

#Dictionaries
md = {'state':'MD', 'population':5.796e6}
print(md['state'])

for key in md:
    print('{:12s} --> {}'.format(key, md[key]))

#Assigning keys and values
md['flower'] = 'Sunflower'
print(md)

print(md.keys())
for key in md.keys():
    print(key,md[key])


goog = {'acquired': '2015-01-15',
        'broker': 'Roberto Cruz',
        'price': 521.78,
        'shares': 100,
        'location': 'here',
        'symbol': 'GOOG'}
for key in sorted(goog.keys()):
    print(goog[key])

for key, value in goog.items():
    print('{:12s} --> {}'.format(key, value))

if 'sold' in goog:
    v = goog['sold']
else:
    v = 'missing'
print(v)

v = goog.get('sold', 'missing')
print(v)

#More Information: Choosing Data Structures
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016]
federal = [3457079000., 3603059000., 3536951000., 3454647000., 3506089000., 3758577000., 3999467000.]
edu = [94169000., 67584000., 59605000., 41882000., 60917000., 104189000., 69939000.]
research = [11730000., 12434000., 12458000., 12479000., 12011000., 12271000., 12824000.]
soc = [706737000., 730811000., 773290000., 813551000., 850533000., 896294000., 944338000.]
defense = [666703000., 678064000., 650851000., 607795000., 577897000., 567703000., 586479000.]
for i in range(len(years)):
    percent = (edu[i] + research[i])/federal[i] * 100
    if percent >= 3:
        print(years[i], percent)

budgets = []
for year, f, r, s, e, d, in zip(years, federal, research, soc, edu, defense):
    # Each year is a dictionary
    budgets.append({
        'year':year,
        'federal':f,
        'research':r,
        'soc':s,
        'edu':e,
        'defense':d
    })
for budget in budgets:
    percent = (budget['edu'] + budget['research'])/budget['federal'] * 100
    if percent >= 3:
        print(budget['year'], percent)
    
for thing in budgets:
    print(type(thing))
for thing in budgets:
    print(thing.keys())
for key,value in budgets[0].items():
    print("%s: %s" % (key, type(value)))

#Slicing
integers = list(range(1, 11))
print(integers)

subset = integers[0:3]
print(subset)

print(integers[2:6])
print(integers[4:-2])
print(integers[-3])
print(integers[2])
print(integers[:4] + integers[4:])

#Strides
print(integers[0:6:2])
print(integers[2::3])
print(integers[:7:2])
print(integers[::4])

#Reversal
print(integers[::-1])
print(integers[-0:-11:-1])

#Strings are containers
song = "I'm a lumber jack and I'm OK."
print(song[4])
print(song[::-1])

#Lists
fibonacci = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
print(fibonacci[1::3])

#Strings
words = "Actions, Changed, Things"
words[::9]

#len
print(len(integers))
print(len(song))

md = {"state":'MD', 'flower':'sunflower'}
print(len(md))

print(sum(integers[::2]))
print(sum(integers[1::2]))
print(sum(integers))

#sorted
print(sorted(md.keys()))

more_numbers = [20, 423.2, -1.2, 2, 4, 3, 10, 8]
sorted_numbers = sorted(more_numbers)
print(sorted_numbers)

sorted_chars = sorted(song)
print(sorted_chars)

#min and max
print(max(more_numbers))
print(min(more_numbers))
print(max(song))
print(min(song))

#Lists
the_words = '''We choose to go to the moon in this decade and do the other things, 
not because they are easy, but because they are hard, 
because that goal will serve to organize and measure the best of our energies and skills, 
because that challenge is one that we are willing to accept, one we are unwilling to postpone, 
and one which we intend to win.'''
wordlist=the_words.replace(',','').split()
print(wordlist)

newlist = []
for word in wordlist:
    if 's' in word:
        newlist.append(word)
print(newlist)

new_list = [word for word in wordlist if 's' in word]
print(new_list)

#Roll the dice 100 times.
#Collect only the odd numbers.
#How many did you find?
rolls = [random.randint(1,6) for _ in range(100)]
odd = [r for r in rolls if r % 2 != 0]
len(odd)

