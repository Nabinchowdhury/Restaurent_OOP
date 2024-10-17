class Order:
    def __init__(self, customer, items) -> None:
        self.customer = customer
        self.items = items
        self.bill = 0
        for item in items:
            self.bill += item.price