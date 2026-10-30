class Animal:
    def walk(self):
        print("walking...")


class dog(Animal):
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def bark(self):
        print("woof!")
roger = dog("Roger",8)
print(type(roger))

print(roger.name)
print(roger.age)
print(roger.bark())
print(roger.walk())

