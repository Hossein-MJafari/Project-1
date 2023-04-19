# this class reads main wearhouse.csv and returns a pandas dataframe
from ast import Try
import pandas as pd
import numpy as np
# from order import Order


class Status:
    def __init__(self):
        self.a = pd.read_csv("main wearhouse.csv")

    def show_status(self):
        print(self.a)

# this class updates the dataframe after each order.
# class Auto_Update:
#      self.cart[product_name]


# this class updates the dataframe when the admin wants, either with file or terminal input.
class Manual_Update:

    def __init__(self, warehouse_file):
        self.warehouse_file = warehouse_file
        self.stock = pd.read_csv(warehouse_file, dtype={
                                 'id': int, 'current_stock': int, 'wearhouse_id': int})

    def update_with_file(self, update_file):
        if update_file.endswith('.csv'):
            update_df = pd.read_csv(
                update_file, dtype={'item_id': int, 'new_stock': int})

            for _, row in update_df.iterrows():
                item_id = row['id']
                quantity = row['new_stock']

                if item_id in self.stock.index:
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
            print(update_df)
            print(self.stock)
        elif update_file.endswith('.txt'):
            with open(update_file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    item_id, quantity = line.strip().split(', ')
                    item_id = item_id
                    quantity = quantity
                    if item_id in self.stock.index:
                        # Calculate equal distribution
                        equal_quantity = quantity // 3
                        remaining_quantity = quantity % 3

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
                    print(line)
                    print(self.stock)
        else:
            print("File Not Supported. Supported Files: (.txt/.csv)")

    def update_with_terminal(self):
        while True:
            item_id = input('Enter item ID (or "done" to finish): ')
            if item_id == 'done':
                break
            try:
                item_id = int(item_id)
                size = input(f'Enter size for item {item_id}: ')
                if size in ['s', 'm', 'l']:
                    try:
                        quantity = int(
                            input(f'Enter quantity for the item {item_id} with the size of {size}: '))
                        self.stock.loc[(self.stock['id'] == item_id) & (
                            self.stock['size'] == size), 'current_stock'] = quantity
                    except ValueError:
                        print(
                            "Value for quantity of the item should be a number!\nTry Again")
                else:
                    print("Not a suppoted size! Supported sizes are:\ns\nm\nl")

            except ValueError:
                print("Not a Valid Command!")

            print(self.stock)

    def save_stock(self):
        self.stock.to_csv(self.warehouse_file, index=False)

# testing the Manual_Update()


upwh = Manual_Update("main wearhouse.csv")
# upwh.update_with_file("update stock.csv")
# upwh.update_with_file("update stock.txt")
# upwh.update_with_terminal()
# upwh.save_stock()


# this class lets the admin to add new merch to the store.
class Add_Stock:
    pass
