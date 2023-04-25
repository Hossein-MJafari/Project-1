# from wearhouse import
import pandas as pd
from order import Cart, Payment_data
from wearhouse import Update ,Auto_Update
from banking import Output
from logistic import Logistics , Time
if __name__ == '__main__':
    class Start(Update):

        def start(self):
            print("Account mode: \n 1.customer \n 2.seller")
            acount_mode = int(input("Enter your choice: "))

            if acount_mode == 1:
                while True:
                    print("Customer Mode Menu:")
                    print("1.show available products")
                    print("2.show your cart")
                    print("3.payment")
                    print("0.exit customer mode")
                    customer_menu = int(input("Enter your choice: "))
                    if customer_menu == 1:
                        return pd.read_csv("main wearhouse.csv")
                        status = "Continue"
                        while status != "Finish":
                            product_name = input("Enter product name:")
                            size = input("Enter product's size: ")
                            quantity = input("Enter product's quantity: ")
                            Cart.add_to_cart(product_name, size, quantity)
                            status = input("Continue Or Finish")
                    elif customer_menu == 2:
                        return Cart.cart
                    elif customer_menu == 3:
                        if Cart.cart.values() == None:
                            print("Your cart is empty!")
                        else:
                            name = input("Enter your name: ")
                            phone_number = input("Enter your phone number: ")
                            address = input("Enter your address: ")
                            delivery_time = input("Enter your delivery_time: ")
                            order_object = Payment_data(name, phone_number, address, delivery_time)
                            card_number = input("Enter your card number: ")
                            city = input("Enter your city: ")
                            state = input("Enter your state: ")
                            postal_code = input("Enter your postal code: ")
                            address_detail = input("Enter your address detail: ")
                            logistics_object = Logistics(city, state, postal_code, address_detail)
                            time_object = Time.telling_time(delivery_time)
                            order_object.make_payment(card_number)
                            Auto_Update.auto_update()
                            return #factor
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
                        super().__init__()
                        print('we have 2 options to update wear house: ')
                        print('1:giving csv')
                        print('2:giving informations')
                        seller_choice = int(input('Enter your choice:'))

                        if seller_choice == 1:
                            super().update_stock_from_csv()
                            # return Manual_Update.update_stock_from_csv()

                        elif seller_choice == 2:
                            super().update_stock_from_terminal()
                            # return Manual_Update.update_stock_from_terminal()

                        else:
                            print("Invalid choice! Try again...")
                    elif seller_menu == 2:
                        return Output
                    elif seller_menu == 0:
                        break
                    else:
                        print("Invalid choice! Try again...")
            else:
                print("Invalid choice!")
