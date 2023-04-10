#this class reads main wearhouse.csv and returns a pandas dataframe
import pandas as pd
class Get_Status:
    def __init__(self):
        self.a = pd.read_csv("main wearhouse.csv")
    def show_status(self):
        print(self.a)

#this class updates the dataframe after each order.
class Auto_Update:
    pass

#this class updates the dataframe when the admin wants, either with file or terminal input.
class Manual_Update:

    def __init__(self, warehouse_file):
        self.warehouse_file = warehouse_file
        self.stock = pd.read_csv(warehouse_file, index_col=0)

    def update_stock_from_csv(self, update_file):

        update_df = pd.read_csv(update_file)

        for _, row in update_df.iterrows():
            item_id = row['id']
            quantity = row['new_stock']

            if item_id in self.stock.index:
                while quantity != 0:
                    current_stock = self.stock.loc[item_id, 'current_stock']
                    min_stock = current_stock.min()
                    # we have to add functionality for the min_stock in a way that this loop finds the min every iteration and adds 1 to that, but for now this WRONG attempt exists:
                    self.stock.loc[item_id, 'current_stock'] += 1
                    quantity -= 1
        # here you can see that the approach to updating is WRONG, becuase the number is added to every size of the stock each time.
        print(update_df)
        print(self.stock)


    def update_stock_from_terminal(self):
        while True:
            item_id = input('Enter item ID (or "done" to finish): ')
            if item_id == 'done':
                break
            size = input(f'Enter size for item {item_id}: ')
            quantity = int(input(f'Enter quantity for item {item_id} size {size}: '))
            self.stock.at[item_id, size] = quantity

    def save_stock(self):
        self.stock.to_csv(self.warehouse_file)

upw = Manual_Update("main wearhouse.csv")
upw.update_stock_from_csv("update stock.csv")
# print(upw.stock)

#this class lets the admin to add new stock to the store.
class Add_Stock:
    pass