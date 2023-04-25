from order import Payment_data, Cart, Factor
from logistic import Time
import csv

with open("orders.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(['quantity', 'order_number', 'pure_price', 'sent_price', 'tax'])
        
        
class Banking(Payment_data):
     def cheking_card(self):
          super().make_payment()
          total_quantity=0
          if self.result == 'Payment was successful!':
               for i in Cart.cart.values():
                    for j in Cart.cart.values():
                         total_quantity += j
                  
               writer.writerow([total_quantity, Payment_data.order_ID, Factor.pure_price, Time.price, Factor.pure_price * 0.09])
           
          else:
               pass
with open('orders.csv','r') as file:
     reader = csv.reader(file)
     
     
class Output:
     def output(self):
          return reader
