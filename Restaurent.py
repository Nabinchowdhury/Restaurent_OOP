class Restaurent:
    def __init__(self, name, rent, menu = []) -> None:
        self.name = name
        self.orders= []
        self.chef = None
        self.server = None
        self.manager = None
        self.rent = rent
        self.menu = menu
        self.revenue = 0
        self.expense = 0
        self.balance = 0
        self.profit = 0

    def add_employee(self, employee_type, employee):
        match employee_type:
            case 'chef':
                self.chef = employee
            case 'server':
                self.server = employee
            case 'manager':
                self.manager = employee
    
    def add_order(self, order):
        self.orders.append(order)

    def receive_payment(self, order, amount, customer):
        if amount >= order.bill:
            self.revenue += order.bill
            self.balance += order.bill
            customer.due_amount = 0
            return amount - order.bill
        else:
            print('Not enough Money, give more')
        
    def pay_expense(self, amount, description):
        if amount < self.balance:
            self.expense += amount
            self.balance -= amount
            print(f'Expense {amount} for {description}')
        else:
            print(f'Not enough money to pay {amount} for {description}')
    
    def pay_salary(self, employee):
        if employee.salary < self.balance:
            employee.receive_salary(employee.salary)
            self.expense += employee.salary 
            self.balance -= employee.salary 
    
    def show_employees(self):
        print('-----------------------------')
        if self.chef is not None:
            print(f"{self.name}'s Chef is {self.chef.name}, salary {self.chef.salary}")
        if self.manager is not None:
            print(f"{self.name}'s manager is {self.manager.name}, salary {self.manager.salary}")
        if self.server is not None:
            print(f"{self.name}'s server is {self.server.name}, salary {self.server.salary}")
        print('-----------------------------')