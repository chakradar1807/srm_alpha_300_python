from phone import phone

# class keyborad(Item):
#     pay_rate = 0.7
#     def __init__(self,name: str, price:float, quantity=0):

#         super().__init__(
#             name,price,quantity

#         )


from keyboard import keyboard

item1 = keyboard("jscKeyboard",1000,3)

item1.apply_discount()
print(item1.price)

