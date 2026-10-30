name = "ChaKri"
print(isinstance(name,str))

number = "20"
age = int(number)
print(isinstance(age,int))

# complex for complex numbers 
# bool for dooleans
# list for lists
# tuple for tuples
# range for ranges 
# dict for dictionaries
# set for sets

# boolean operators... and not or 

print(name)
print(name.lower())
abd = ('chak')
print(abd)
print(abd[1:3])

area = 300000.45143
print(round(area,3))

from enum import Enum

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(State.ACTIVE.value)
print(State(1))
print(State['ACTIVE'])

age = input("what is your age? ")
print("your age is " + age)




