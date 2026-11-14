import csv

class Item:

    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero! "
 

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
       
       
       with open('items.csv','r',) as f:
          
          
          reader = csv.DictReader(f)
          items = list(reader)

    

       for item in items:
        Item( name=item.get('name'),price=int(item.get('price')),quantity=int(item.get('quantity')),
             )
     
    def __repr__(self):
            return f"Item('{self.name}',{self.price},{self.quantity})"    

Item.instantiate_from_csv()

print(Item.all)


# item1 = Item("phone", 100, 1)
# item2 = Item("laptop", 1000, 3)
# item3 = Item("cable", 10, 5)
# item4 = Item("mouse", 50, 5)
# item5 = Item("keyboard", 75, 5)

# for instance in Item.all:
#     print(instance.name)

# print(Item.all)
