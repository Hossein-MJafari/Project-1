import pandas as pd
from order import *
from wearhouse import *
from banking import *
from logistic import *


Update_obj = Update("main wearhouse.csv")
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
                    print("0.exit store")
                    customer_menu = int(input("Enter your choice: "))
                    if customer_menu == 1:
                        cart_object = Cart()
                        print(pd.read_csv("main wearhouse.csv"))
                        status = "Continue"
                        while status != "Finish":
                            product_name = input("Enter product name: ")
                            size = input("Enter product's size: ")
                            quantity = int(input("Enter product's quantity: "))
                            cart_object.add_to_cart(database, product_name, size, quantity)
                            status = input("Continue Or Finish? ")
                    elif customer_menu == 2:
                        try:
                            print(cart_object.cart)
                        except:
                            print("Your cart is empty!")
                    elif customer_menu == 3:
                        try:
                            len(cart_object.cart)
                        except:
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
                            time_object = Time(delivery_time)
                            order_object.make_payment(card_number)
                            Update_obj.auto_update(order_object)
                            Banking.cheking_card()
                            factor_object = Factor(order_object, cart_object)
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
                        update_wearhouse = input('give your csv file path:')
                        wearhouse_object = Update(update_wearhouse)
                        print('we have 2 options to update wear house: ')
                        print('1:giving csv')
                        print('2:giving informations')
                        seller_choice = int(input('Enter your choice:'))

                        if seller_choice == 1:
                            wearhouse_object.update_with_file(update_wearhouse)
                            # return Manual_Update.update_stock_from_csv()
                            wearhouse_object.save_stock()
                        elif seller_choice == 2:
                            wearhouse_object.update_with_terminal()
                            # return Manual_Update.update_stock_from_terminal()
                            wearhouse_object.save_stock()
                        else:
                            print("Invalid choice! Try again...")
                    elif seller_menu == 2:
                        Output.output()
                    elif seller_menu == 0:
                        break
                    else:
                        print("Invalid choice! Try again...")
            else:
                print("Invalid choice!")


start = Start("main wearhouse.csv")
start.start()