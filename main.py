from wearhouse import Get_Status
import pandas as pd
from order import Cart, Payment_data
if __name__ == '__main__':

class Start:
   def start(self):
       print("Account mode: \n 1.customer \n 2.seller")
       acount_mode = int (input("Enter your choice: "))

       if acount_mode == 1:
           while True:
               print("Customer Mode Menu:")
               print("1.show available products")
               print("2.show your cart")
               print("3.payment")
               print("0.exit customer mode")
               customer_menu = int(input("Enter your choice: "))
               if customer_menu == 1 :
                   return pd.read_csv("main wearhouse.csv")
               elif customer_menu == 2:
                   return Cart.cart
               elif customer_menu == 3:
                   return Payment_data
               elif customer_menu == 0:
                   break
               else:
                   print("Invalid choice! Try again...")

       elif acount_mode == 2:
           while True:
               print("Seller Mode Menu:")
               print("1.Wearhouse")
               print("2.Banking")
               print("0.Exit seller mode")
               seller_menu = int(input("Enter your choice: "))
               if seller_menu == 1:
                   pass
               elif seller_menu == 2:
                   pass
               elif seller_menu == 0:
                   break
               else:
                   print("Invalid choice! Try again...")

       else:
           print("Invalid choice!")