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
    pass

#this class lets the admin to add new stock to the store.
class Add_Stock:
    pass