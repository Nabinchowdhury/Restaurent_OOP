from Menu import Pizza, Burger, Drinks, Menu
from Restaurent import Restaurent
from Users import Manager, Chef, Server
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
    chef = Manager('rustom baburchi', 4321, 'Rustom@baburchi.com', 'rustam dighi', 300, '1 Feb, 2020', 'chef')
    restaurent.add_employee('chef', chef)
    server = Manager('chota server', 2143, 'chotu@chikna.com', 'choto rastar more', 100, '1 March, 2020', 'server')
    restaurent.add_employee('server', server)
    
    restaurent.show_employees()

if __name__ == '__main__':
    main()