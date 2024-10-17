from Menu import Pizza, Burger, Drinks, Menu
from Restaurent import Restaurent
from Users import Manager, Chef, Server, Customer
from Order import Order
def main():
    menu = Menu()
    pizza_1 = Pizza('sausage pizza', 500, 'large', ['sausage', 'sauase', 'onion'])
    menu.add_menu_item('pizza', pizza_1)
    pizza_2 = Pizza('chicken pizza', 600, 'large', ['chicken', 'onion', 'oil'])
    menu.add_menu_item('pizza', pizza_2)
    pizza_3 = Pizza('veg pizza', 400, 'large', ['potato', 'onion', 'oil'])
    menu.add_menu_item('pizza', pizza_3)

    burger_1 = Burger('naga burger', 500, 'chicken', ['bread', 'sauase', 'onion'])
    menu.add_menu_item('burger', burger_1)
    burger_2 = Burger('veg burger', 600, 'ver', ['veg', 'onion', 'oil'])
    menu.add_menu_item('burger', burger_2)

    coke = Drinks('coke', 50, True)
    menu.add_menu_item('drinks', coke)
    coffee = Drinks('coffee', 100, False)
    menu.add_menu_item('drinks', coffee)

    menu.show_menu()

    restaurent = Restaurent('new restaurent', 2000, menu)
    manager = Manager('kala chan manager', 1234, 'kala@Chan.com', 'kalia bazar', 1000, '1 Jan, 2020', 'manager')
    restaurent.add_employee('manager', manager)
    chef = Chef('rustom baburchi', 4321, 'Rustom@baburchi.com', 'rustam dighi', 3000, '1 Feb, 2020', 'chef', 'everything')
    restaurent.add_employee('chef', chef)
    server = Server('chota server', 2143, 'chotu@chikna.com', 'choto rastar more', 100, '1 March, 2020', 'server')
    restaurent.add_employee('server', server)
    
    restaurent.show_employees()

    customer_1 = Customer('sabik', 5000, 9876, 'sakib@khan.com', 'onek dure')
    order_1 = Order(customer_1, [pizza_1, coke, pizza_2, pizza_3, burger_1, burger_2, coffee])
    customer_1.pay_for_order(order_1) 
    restaurent.add_order(order_1)
    amount_returned = restaurent.receive_payment(order_1, 10000, customer_1)
    print(amount_returned, f'to {customer_1.name}')

    customer_2 = Customer('nabik', 5000, 9876, 'nakib@khan.com', 'onek bohu dure')
    order_2 = Order(customer_2, [pizza_1, coke, pizza_2, pizza_3, burger_1, burger_2, coffee])
    customer_2.pay_for_order(order_2) 
    restaurent.add_order(order_2)
    amount_returned = restaurent.receive_payment(order_2, 20000, customer_2)

    print(amount_returned, f'to {customer_2.name}')
    print('revenue', restaurent.revenue, 'restaurent balance', restaurent.balance)
    
    restaurent.pay_expense(restaurent.rent, 'rent')
    print('after rent revenue', restaurent.revenue, 'restaurent balance', restaurent.balance)
    
    print(f'before salaray chef due {chef.due}')
    restaurent.pay_salary(chef)
    print('after salary revenue', restaurent.revenue, 'restaurent balance', restaurent.balance)
    print(f'after salaray chef due {chef.due}')

if __name__ == '__main__':
    main()