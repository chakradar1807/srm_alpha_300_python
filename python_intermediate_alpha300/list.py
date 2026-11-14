# list
list_org = ["banana","cherry","apple"]

list_copy = list_org[:]

list_copy.append("lemon")

print(list_copy)
print(list_org)

mylist = [1, 2,3,4,5,6,7,8,9,0,]
b = [x*x for x in mylist]

print(mylist)
print(b)
# tuple
mytuple = tuple(["max",28,"boston"])
print(mytuple)
if "tim" in mytuple:
    print("yes")
else:
    print("no")    
item = mytuple[-2]
print(item)

my_tuple = ('a','e','i','o','u')
print(my_tuple.index("o"))

c = my_tuple[::-2]
print(c)

import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]",number=1000000))


import sys
My_list =[0,1,2,"hello",True]

print(sys.getsizeof(My_list),"bytes")
print(sys.getsizeof(my_tuple),"bytes")

# dictionary
mydict = {"name": "max","age":28,"city":"newyork"}
print(mydict)

mydict["email"] = "max@xyz.com"
print(mydict)

mydict["email"] = "coolmax@xyz.com"
print(mydict)

# del mydict["name"]
# print(mydict)

mydict.popitem()
print(mydict)

if "name" in mydict:
    print(mydict["name"])

try:
    print(mydict["name"])
except:
    print("error")

my_dict = {3: 9,6:36,9:81}
print(my_dict)

value = my_dict[3]
print(value)

# sets
myset = set()

myset.add(1)
myset.add(30)
myset.add(2)

myset.pop()
myset.discard(2)

print(myset)

odds = {1,3,5,7,9,11,13}
evens = {2,4,6,8,10,12}
primes = {2,3,5,7,11}

u = odds.union(evens)
print(u)

v = evens.intersection(u)
print(v)

odds.update(primes)
print(odds)

evens.intersection_update(primes)
print(evens)

print(primes.issubset(odds))

a =frozenset([1,2,3,4,5])
# a.remove(2)
print(a)

#  string
my_string = "I am a programmer"
print(my_string)

substring = my_string[::-2]
print(substring)

greeting = "hello"
if 'e' in greeting:
    print('yes')
else:
    print('no')

string = '    Hello World , you guys doing well!   '
string = string.strip()
print(string)
print(string.lower())

print(string.upper())

string = string.replace('world','universe')
print(string)
print(string.startswith('h'))

print(string.endswith('world'))
print(string.find('o'))

print(string.count('p'))

string = string.split(" ")
new_string = ''.join(string)

print(new_string)

from collections import Counter
a = "aaaabbbccc"
my_counter = Counter(a)
print(my_counter)
print(list(my_counter.elements()))

from collections import namedtuple
point = namedtuple('point','x,y')
pt = point(1,-4)
print(pt.x, pt.y)

from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['a'] = 1
print(ordered_dict)

from collections import defaultdict
d = defaultdict(list)
d['a'] = 1
d['b'] = 2
print(d['c'])

from collections import deque
d = deque()

d.append(1)
d.append(2)

d.appendleft(3)
print(d)

d.extend([4,5,6])
print(d)

d.rotate(-1)
print(d)

from itertools import product
a =[1,2]
b =[3,4]
prod = product(a,b)
print(list(prod))

from itertools import permutations
a = [1,2,3]
perm = permutations(a,3)
print(list(perm))

from itertools import combinations
a = [1,2,3,4]
comb = combinations(a,2)
print(list(comb))


from itertools import accumulate
a = [1,2,3,4]
acc = accumulate(a)
print(a)
print(list(acc))


from itertools import groupby
def smaller_than_3(x):
    return x < 3
a = [1,2,5,3,4]
group_obj = groupby(a,key = smaller_than_3 )
for key, value in group_obj:
    print(key, list(value))

from itertools import count,cycle,repeat
for i in count(10):
    print(i)
    if i == 15:
        break

# for i in cycle(a):
#     print(i)

for i in repeat(1,4):
        print(i)

add10 = lambda x:x + 10
print(add10(5))

def add10_func(x):
    return x + 10

mult = lambda x,y: x*y
print(mult(2,7))
