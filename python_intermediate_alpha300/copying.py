import copy

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Company:
    def __init__(self,boss,employee):
        self.boss = boss
        self.employee = employee

p1 = person('Alex', 55)
p2 = person('Joe',27)

company = Company(p1,p2)
company_clone = copy.deepcopy(company)
company_clone.boss.age = 56
print(company_clone.boss.age)
print(company.boss.age)
