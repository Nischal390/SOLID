class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return total
    

class OrderManager:
    def place_order(self, order):
        total = order.calculate_total()
        print(f'total is: {total}')

order_items = [
    Item("Product 1", 10),
    Item("Product 2", 20),
    Item("Product 2", 15)
]

order = Order(123, order_items)
order_manager = OrderManager()
order_manager.place_order(order)