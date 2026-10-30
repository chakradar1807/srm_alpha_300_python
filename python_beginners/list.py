# dogs = ["Roger","yashu","syd","quincy","ujwal"]

# dogs[2] = "beau"
# dogs.extend(["judah","chakri"])
# # dogs += ["judah",5] # square bracket is imp or else it will print j u d a h 
# print(dogs)
# dogs.remove("judah")
# print(dogs)
# print(dogs.pop())
# dogs.sort()
# print(dogs)

    #------------------------#

names = ("Roger","syd","Beau")

names[-1]
names.index("Roger")

len(names)

print("Roger" in names)
print(sorted(names))
newTuple = names + ("Tina","Quincy") 

dog = {"name": "Roger","age": 8, "color": "green"}
dog["favorite food"] = "Meat"
del dog['color']

print(dog)


set1 = {"roger,syd"}
set2 = {"roger"}

mod = set1 < set2
print(list(set1))

def hello(name):
    print("hello" + name)
hello(" Beau")
hello(" quincy")

