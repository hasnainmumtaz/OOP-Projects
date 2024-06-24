# Libraries
import os
import time

# Hard coded menu
menu = {
    'Cake' : 5,
    'Icecream' : 3,
    'Cookies' : 2.5,
    'Smoothie' : 2,
    'Brownie' : 4,
    'Ice': 1,
}

# List of orders
orders_recieved = []

# Class Order
class Order:
    order_no = 1
    def __init__(self) -> None:
        self.id = Order.order_no
        self.lst = []
        self.total = 0
        Order.order_no += 1

    # Add Item to order
    def add_item(self,item):
        if item in menu:
            self.lst.append(item)
            self.total += menu[item]
        else:
            print(f'{item} not in menu')

    # Dunder method for string representation
    def __str__(self):
        self.count = dict()
        for item in self.lst:
            if item not in self.count:
                self.count[item] = 1
            else:
                self.count[item] += 1
        order_string = ''
        for (key,value) in self.count.items():
            order_string = order_string + f' {value}x {key},'

        return f'{self.id} -> {self.total} | {order_string}'

# Prints Menu
def print_menu():
    index = 0
    print('------Menu------')
    for name in menu:
        index += 1
        print(f"{index}. {name} | {menu[f'{name}']}")
    print('----------------')

# Main() is the CLI for this Cafe
def main():
    os.system('cls')
    print(f'Cafe Management System\n 1. Make a new Order \n 2. Get All Orders\n 3. Exit')
    option = input('Select an Option:')
    if option == '1':
        order = Order()

        def edit(order):
            os.system('cls')
            print_menu()
            print(f'Current Order: {order.lst}\n Order Total: {order.total}')
            print(f'1. Add item\n2. Finalize\n3. Cancel')
            print('---------------------')
            order_option = input("Select an Option: ")
            if order_option == '1':
                order.add_item(input('Item name: '))
                edit(order)
            elif order_option == '2':
                orders_recieved.append(order)
                print(f'Your order with id {order.id} has been created!')
                main()
            elif order_option == '3':
                print("Order cancelled")
                main()
            else:
                print('Please Input the right option')
                time.sleep(2)
                edit(order)

        
        edit(order)
    
    elif option == '2':
        for order in orders_recieved:
            #print(f'{order.id}) ${order.total} | {order.lst}')
            print(order)

        input("Press Enter to Continue!")
        main()

    elif option == '3':
        os.system('cls')
        exit()
                
main()