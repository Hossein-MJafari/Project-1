from order import Payment_data, Cart, Factor
from logistic import Time, sent_price
import csv

with open("orders.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(['quantity', 'order_number', 'pure_price', 'sent_price', 'tax'])
        
        
class Banking(Payment_data):
    def cheking_card(self):
        super().make_payment()
        if self.result == 'Payment was successful!':
           
             writer.writerow([Cart.cart[product_name][size], Payment_data.order_ID, Factor.pure_price, Time.price, Factor.pure_price * 0.09])
           
        else:
             pass
with open('orders.csv','r') as file:
     reader = csv.reader(file)
     
     
class Output:
     def output(self):
          return reader
