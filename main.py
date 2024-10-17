from Menu import Pizza, Burger, Drinks, Menu
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
if __name__ == '__main__':
    main()