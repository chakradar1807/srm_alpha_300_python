# print("i like pizza")
# print("It's very good!")
# first_name = "chakradar"
# food = "burger"
# email = "chakri123@gmail.com"

# print(f"hello {first_name}")
# print(f"You like {food}")
# print(f"email is {email}")

# age = 25
# quantity = 3
# gpa = 7.9
# print(f"your age is {age}")
# print(f"i need {quantity} of rulers")
# print(f"your cgpa:{gpa}")

# is_student = True
# if is_student:
#     print("you are student")
# else:
#     print("you are not student")    

#                     # variables-string,integer,float,boolean....    

# print(type(is_student))
# print(type(age))

# gpa = int(gpa)
# print(gpa)

# name = ""
# name = bool(name)
# print(name)

                    #typecasting str(),int(),float(),bool()


# srname = input("what is your name: ")
# age = input("what is your age: ")

# print(f"hello{srname}")
# # print(f"your age is {age}")
# age = int(age)
# age = age+1
# print(f"your age is {age}")
#------------------------ # input() = function allows to user to enter value

# length = float(input("enter length of rectangle: "))
# width = float(input("enter width of rectangle: "))
# area = length * width 
# abd = width / length
# abd = (int(abd))


# print(f"area of rectangle is {area}cm^2")
# print(abd)  
#---------------------------------#
# import math 
# radius = float(input("enter the radius of a circle: "))
# circumference = 2 * math.pi * radius
# area = math.pi * pow(radius, 2)

# print(f"the circumference is: {round(circumference, 2)}cm")
# print(f"the area of circle is:{round(area, 2)}cm^2")

#--------------------------------#
# import math

# a = float(input("enter side a : "))
# b = float(input("enter side b: "))

# c = math.sqrt(pow(a,2) + pow(b,2))

# print(c)
#-----------------------------#
# age = int(input("enter your age: "))

# if age >= 18:
#     print("your are major!")
# else:
#     print("you are minor!")

# response = input("would you like to eat? (Y/N): ") 

# if response == "Y":
#     print("have some food!")

# elif response != "Y" and response != "N":
#     print("entered value is wrong!")

# else:
#     print("go to work!")

# ---------------------#

# operator = input("enter an operator(+ - * /): ")
# num1 = float(input("enter 1st number: "))
# num2 = float(input("enter 2nd number: "))

# if operator != "+" and operator != "-" and operator != "*" and operator != "/":
#     print("entered value is wrong")

# elif operator == "+":
#     result = num1 + num2
#     print(round(result,3))
# elif operator == "-":
#     result = num1 - num2
#     print(round(result,3)) 
# elif operator == "*":
#     result = num1 * num2
#     print(round(result,3)) 
# else:
#     result = num1 / num2
#     print(round(result,3))          

# ----------------------------#

# weight = float(input("enter your weight: "))
# unit = input("kilograms or pounds? (k or l):" )

# if unit == "k":
#     weight = weight * 2.205
#     print(f"your weight is: {round(weight,1)}Lbs")
# elif unit == "l":
#     weight = weight / 2.205
#     print(f"your weight is {round(weight,1)}kgs")   
# else:
#     print(f"{unit}was not valid")

#-----------------------#

# unit = input("is this temperature is in celsius or fahrenheit (c/f): ")
# temp = float(input("enter the temperature: "))
# if unit == "c":
#     temp = round((9 * temp) / 5 + 32,1)
#     print(f"the temperature in fahrenheit is:{temp}F")
# elif unit == "f":
#     temp = round((temp - 32) * 5 / 9,1)
#     print(f"the temperature in celsius is: {temp}C")
# else:
#     print(f"{unit} is not valid of measurement")

#-----------------------------#
temp = 25
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print("the outdoor event is cancelled")
else:
    print("the outdoor event is scheduled")



