products = ['apple', 'banana', 'orange', 'grape', 'pear']
prices = [1.2, 3.3, 2.1, 4.5, 3.2]
quantities = [300, 250, 400, 500, 350]

def main():
    running = True
    while running:
        print_menu()
        choice = int(input('Enter your choice: '))
        if choice == 1:     add_fruit()
        elif choice == 2:   edit_price()
        elif choice == 3:   sell_fruit()
        elif choice == 4:   delete_fruit()
        elif choice == 5:   running = exit()
        else:               print('Invalid choice. Please try again.')

def print_menu():
    print('1. Add fruit')
    print('2. Edit price')
    print('3. Sell fruit')
    print('4. Delete fruit')
    print('5. Exit')

def show_fruit():
    print('+----+----------+----------+----------+')
    print(f'|{"No":^4}|{"Product":^10}|{"Price":^10}|{"Quantity":^10}|')
    print('+----+----------+----------+----------+')
    for i in range(len(products)):
        print(f'|{i+1:^4}|{products[i]:>10}|{prices[i]:>10.2f}|{quantities[i]:>10}|')
        print('+----+----------+----------+----------+')

def add_fruit():
    # call show_fruit() to display the current list of fruits
    show_fruit()
    # ask user to enter a fruit name
    fruit = input('Enter fruit name: ').lower()
    if fruit in products:
        print('Fruit already exists.')
        return
    # ask user to enter price
    price = float(input('Enter price: '))
    # ask user to enter quantity
    quantity = int(input('Enter quantity: '))
    
    products.append(fruit)  # append the new fruit name to the products list
    prices.append(price)    # append the new price to the prices list
    quantities.append(quantity) # append the new quantity to the quantities list

def enter_fruit():
    show_fruit()
    fruit = input('Enter fruit name: ').lower()
    if fruit not in products:
        print(f'{fruit} not found.')
        return -1, fruit
    
    index = products.index(fruit)   # get the index of the fruit
    return index

def edit_price():
    index, fruit = enter_fruit()
    if index == -1:
        return
    
    new_price = float(input('Enter new price: '))  # ask user to enter new price
    prices[index] = new_price   # update the price in the prices list
    
    print(f'Price updated for {fruit}.')
    show_fruit()    # call show_fruit() to display the updated list of fruits

def sell_fruit():
    index, fruit = enter_fruit()
    if index == -1:
        return
    
    quantity = int(input('Enter quantity to sell: '))
    if quantity > quantities[index]:
        print('Not enough stock.')
        return
    
    quantities[index] -= quantity   # update the quantity in the quantities list
    
    print(f'{quantity} {fruit} sold.')
    show_fruit()

def delete_fruit():
    index, fruit = enter_fruit()
    if index == -1:
        return
    
    products.pop(index)     # remove the fruit from the products list
    del prices[index]       # remove the price from the prices list
    del quantities[index]   # remove the quantity from the quantities list

    print(f'{fruit} deleted.')
    show_fruit()

def exit():
    answer = input('Are you sure you want to exit? (y/n): ')
    return answer.lower() == 'n'

if __name__ == '__main__':
    main()