class item:
    pay_rate = 0.8
    def __init__(self, name: str, price: float, quantity = 0):
        assert price >= 0
        assert quantity >= 0

        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity
    
item1 = item("Laptop", 1000, 5)
item2 = item("phone", 500, 4)
item3 = item("Mouse", 300, 8)
item4 = item("keyboard", 1500, 10)

print(item1.calculate_total_price())
print(item2.calculate_total_price())
print(item3.calculate_total_price())
print(item4.calculate_total_price())

#********************************************************************
import csv

class item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity = 0):
        assert price >= 0
        assert quantity >= 0

        self.name = name
        self.price = price
        self.quantity = quantity

        item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        # self.price = self.price * item.pay_rate
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"item('{self.name}', '{self.price}', '{self.quantity}')"
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('item.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

            for item in items:
                item(name = item.get("name"),
                        price = float(item.get("price")),
                        quantity = int(item.get("quantity")))
    
item.instantiate_from_csv()
print(item.all)

item1 = item("Laptop", 1000, 5)
item1.pay_rate = 0.9
item1.apply_discount()
print(item1.calculate_total_price())

# #*************************************************************************

item2 = item("phone", 500, 4)
item2.pay_rate = 0.4
item2.apply_discount()
print(item2.calculate_total_price())
# #*************************************************************************

item3 = item("Mouse", 300, 8)
item3.pay_rate = 1.2
item3.apply_discount()
print(item3.calculate_total_price())
# #*************************************************************************

item4 = item("keyboard", 1500, 10)
item4.pay_rate = 0.8
item4.apply_discount()
print(item4.calculate_total_price())

# print(item.all)
# #*************************************************************************

print(item1.calculate_total_price())
print(item2.calculate_total_price())
print(item3.calculate_total_price())
print(item4.calculate_total_price())

item1.apply_discount()
print(item1.price)
print(item1.quantity)

item2.apply_discount()
print(item1.price)
print(item2.quantity)

item3.apply_discount()
print(item1.price)
print(item3.quantity)

item4.apply_discount()
print(item1.price)
print(item4.quantity)