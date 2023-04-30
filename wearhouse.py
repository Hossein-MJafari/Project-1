# this class reads main wearhouse.csv and returns a pandas dataframe
import pandas as pd
import numpy as np
from order import Payment_data, Cart
import csv
# from order import Order


class Status:
    def __init__(self):
        self.read_stat = pd.read_csv("main wearhouse.csv")
        
    def show_status(self):
        print(self.read_stat)

# this class updates the dataframe after each order.


class Auto_Update:
    def auto_update(self):
        main_csv = Status.read_stat
        if Payment_data.payment_status==True:
            for name in Cart.cart.keys():
                for i in Cart.cart[name].keys():
                    size = i
                    for j in Cart.cart[name].values():
                        quantity = j
                    main_csv.loc[(main_csv['stock_name'] == name) & (
                    main_csv['size'] == size), 'current_stock'] -= quantity
    
               
        else:
            pass


# this class updates the dataframe when the admin wants, either with file or terminal input.
class Update:

    def __init__(self, warehouse_file):
        self.warehouse_file = warehouse_file
        self.stock = pd.read_csv(warehouse_file, dtype={
                                 'id': int, 'current_stock': int,'price':float, 'wearhouse_id': int})
        #while True:
         #   #self.approach = input("How do you want to update/add your wearhouses? (file/terminal)\n***Type 'quit' to exit\n")
          #  if self.approach.lower() == "file":
           #     update_file = input("Enter the full directory of the file with its extention(.txt/.csv): ")
            #    self.update_with_file(update_file)
            #elif self.approach.lower() == "terminal":
             #   self.update_with_terminal()
            #elif self.approach.lower() == "quit":
             #   break
            #else:
             #   print("Invalid way of updating. type either 'file' or 'terminal' or 'quit' for exit.")

    def update_with_file(self, update_file):
        if update_file.endswith('.csv'):
            update_df = pd.read_csv(
                update_file, dtype={'item_id': int, 'new_stock': int})

            for _, row in update_df.iterrows():
                item_id = row['id']
                quantity = row['new_stock']
                self.UpdateOrAdd(item_id, quantity)
                # print(self.stock)

        elif update_file.endswith('.txt'):
            with open(update_file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    item_id, quantity = line.strip().split(', ')
                    item_id = int(item_id)
                    quantity = int(quantity)
                    self.UpdateOrAdd(item_id, quantity)
                    # print(self.stock)

        else:
            print("File Not Supported. Supported Files: (.txt/.csv)")

    # the functions update() and UpdateOrAdd() are added becuase their code is used multiple times.
    def update(self, item_id, quantity):
        # Calculate equal distribution
        equal_quantity = (quantity // 3)
        remaining_quantity = (quantity % 3)

        # Distribute equally
        self.stock.loc[(self.stock['id'] == item_id) & (
            self.stock['size'] == 's'), 'current_stock'] = equal_quantity
        self.stock.loc[(self.stock['id'] == item_id) & (
            self.stock['size'] == 'm'), 'current_stock'] = equal_quantity
        self.stock.loc[(self.stock['id'] == item_id) & (
            self.stock['size'] == 'l'), 'current_stock'] = equal_quantity

        # Distribute remaining quantity randomly
        sizes = ['s', 'm', 'l']
        np.random.shuffle(sizes)
        for size in sizes[:remaining_quantity]:
            self.stock.loc[(self.stock['id'] == item_id) & (
                self.stock['size'] == size), 'current_stock'] += 1

    def UpdateOrAdd(self, item_id, quantity):
        item_id = int(item_id)
        quantity = int(quantity)
        if quantity <= 0:
            raise Exception
        stock_ids = []
        counts = []
        for i, count in self.stock['id'].value_counts().items():
            stock_ids.append(i)
            counts.append(count)

        if item_id in stock_ids and counts[stock_ids.index(item_id)] == 3:
            self.update(item_id, quantity)
        else:
            prompt = input(
                f"The item with id '{item_id}' is a new one, would you like to add it to your wearhouse? (yes/no) ")
            if prompt == 'yes':
                # asking for the info to add 3 new rows for our new item in store:
                name = input("Enter the merch's name: ")
                price = float(input("Enter its price: "))
                wearhouse_id = input("Enter the wearhouse id: ")
                new_rows = [
                    {'id': item_id, 'stock_name': name, 'size': 's',
                        'current_stock': quantity, 'price': price, 'wearhouse_id': wearhouse_id},
                    {'id': item_id, 'stock_name': name, 'size': 'm',
                        'current_stock': quantity, 'price': price, 'wearhouse_id': wearhouse_id},
                    {'id': item_id, 'stock_name': name, 'size': 'l',
                        'current_stock': quantity, 'price': price, 'wearhouse_id': wearhouse_id}
                ]
                rows = pd.DataFrame(new_rows)
                self.stock = pd.concat([self.stock, rows], ignore_index=True)

                # Now that we have 3 new rows, we distribute the quantity the same way:
                self.update(item_id, quantity)
        
    def update_with_terminal(self):
        while True:
            item_id = input('Enter the item ID (or "done" to finish): ')
            if item_id == 'done':
                break
            try:
                item_id = int(item_id)

            except ValueError:
                print("Not a Valid Command!")

            else:
                stock_ids = []
                counts = []
                for i, count in upwh.stock['id'].value_counts().items():
                    stock_ids.append(i)
                    counts.append(count)
                if item_id in stock_ids and counts[stock_ids.index(item_id)] == 3:
                    size = input(f'Enter size for item {item_id}: ')
                    if size in ['s', 'm', 'l']:
                        try:
                            quantity = int(
                                input(f'Enter quantity for the item {item_id} with the size of {size}: '))
                        except ValueError:
                            print("Value for quantity of the item should be a number!\nTry Again")
                        else:
                            self.stock.loc[(self.stock['id'] == item_id) & (
                                self.stock['size'] == size), 'current_stock'] = quantity

                    else:
                        print("Not a suppoted size! Supported sizes are:\ns\nm\nl")
                    
                else:
                    try:
                        self.UpdateOrAdd(item_id, quantity=0)
                    except Exception:
                        quantity = input("Enter the new Stock: ")
                        self.UpdateOrAdd(item_id, quantity)


            # print(self.stock)

    def save_stock(self):
        self.stock.to_csv(self.warehouse_file, index=False)


# testing the Manual_Update()

upwh = Update("main wearhouse.csv")
# upwh.update_with_file("update stock.csv")
# upwh.update_with_file("update stock.txt")
# upwh.update_with_terminal()
# upwh.save_stock()
