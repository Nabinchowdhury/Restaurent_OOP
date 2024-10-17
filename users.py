from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, phone, email, address) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name, money, phone, email, address) -> None:
        self.wallet = money
        self.phone = phone
        self.email = email
        self.address = address
        self.__order = None
        super().__init__(name, phone, email, address)

    @property
    def order(self):
        return self.__order
    
    @order.setter
    def order(self, order):
        self.__order = order

    def place_order(self, order):
        self.order = order
        print(f'{self.name} has placed an order {order.items}')
    
    def eat_food(self, order):
        print(f'{self.name} is eating {order.items}')
    
    def pay_for_order(self, amount):
        # TODO: submit money to the manager
        pass

    def give_tips(self, tips_amount):
        pass
    
    def write_review(self, stars):
        pass

class Employee(User):
    def __init__(self, name, phone, email, address, salary, starting_day, department) -> None:
        super().__init__(name, phone, email, address)
        self.salary = salary
        self.starting_day = starting_day
        self.department = department

class Chef(Employee):
    def __init__(self, name, phone, email, address, salary, starting_day, department, cooking_item) -> None:
        super().__init__(name, phone, email, address, salary, starting_day, department)
        self.cooking_item = cooking_item

class Server(Employee):
    def __init__(self, name, phone, email, address, salary, starting_day, department) -> None:
        super().__init__(name, phone, email, address, salary, starting_day, department)
        self.tips_earning = 0
    
    def take_order(self, order):
        pass

    def transfer_order(self, order):
        pass

    def serve_food(self, order):
        pass

    def receive_tips(self, amount):
        self.tips_earning += amount