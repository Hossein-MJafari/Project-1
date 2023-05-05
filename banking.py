from order import *
from logistic import *
import csv

class Banking(Payment_data):

    def __init__(self, name, phone_number, address, delivery_time):
        super().__init__(name, phone_number, address, delivery_time)
        with open("orders.csv", "w") as file:
            self.writer = csv.writer(file)
            self.writer.writerow(
                ['quantity', 'order_number', 'pure_price', 'sent_price', 'tax'])
     #    orders = pd.DataFrame({
     #        "quantity":[],
     #        "order_number":[],
     #        "pure_price":[],
     #        "sent_price":[],
     #        "":[],
            
     #    })

    def cheking_card(self, card_number, cart_object, address):
        super().make_payment(card_number)
        total_quantity = 0
        if self.result == 'Payment was successful!':
            for i in cart_object.cart.values():
                for j in i.values():
                    total_quantity += j
            with open("orders.csv", "w") as file:
               self.writer = csv.writer(file)
               self.writer.writerow([total_quantity, self.order_ID, cart_object.pure_price,
                                   address.price, cart_object.pure_price * 0.09])


with open('orders.csv', 'r') as file:
    reader = csv.reader(file)


class Output:
    def output(self):
        return reader
