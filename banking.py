from order import Payment_data , Cart , Factor
from logistic import Time , sent_price
import csv

with open("orders.csv", "w") as file:
        writer=csv.writer(file)
        writer.writerow(['quantity','order_number','pure_price','sent_price','tax'])
class Banking(Payment_data):
    def cheking_card (self):
        super().make_payment()
        if self.result=='Payment was successful!' :
            #shomare sefaresh to ghesmate factor
            #gheymato havaset bashe
             writer.writerow([Cart.cart[product_name][size], Payment_data.order_ID,Factor.pure_price,Time.price,Factor.pure_price * 0.09])
           
        else :
             pass
with open('orders.csv','r') as file:
     reader=csv.reader(file)
class Output:
     def output(self):
          return reader
          
          











#def is_16_digits(card_number, full_name):
 #   print("Validating your card number...")
  #  if len(str(card_number)) == 16:
   #     with open('payment_result.txt', 'a') as f:
    #        f.write(f'{card_number}\nSuccessful Payment...\n{full_name}\n')
     #   print("Your payment was successful, the payment factor has been created.\nPlease close this window to continue...")
    #else:
     #   with open('payment_result.txt', 'a') as f:
      #      f.write(
       #         f'{card_number}\nUnsuccessful Payment, Try Again...\n{full_name}\n')
       # print("Your payment was unsuccessful, the payment factor has been created.\nPlease close this window to continue...")


#class Validator:
 #   def __init__(self, card_number, full_name):
  #      self.__card_number = card_number
   #     self.__full_name = full_name

