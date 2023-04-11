from wearhouse import Get_Status
import random as rand
class Order:
    def add_to_cart(product_name, size, quantity):
        # Define an empty dictionary to store the cart items
        self.cart = {}
        if product_name in Get_Status().a["stock_name"] and size in Get_Status().a[product_name]["size"]:
            if quantity <= Get_Status().a[product_name][size]["current_stock"]:
                if product_name in cart:
                    self.cart[product_name][1] += quantity
                else:
                    self.cart[product_name][1] = quantity
            else:
                print(f"{quantity} of this item is  not available!")

        else:
            print("This item is not available!")


    pass

class Payment:
    def __init__(self, name, phone_number, address, delivery_time):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.delivery_time = delivery_time
        self.order_ID = rand.randint((10**10), (10**11-1))
        self.payment_status = None

    def make_payment(self, cardـnumber):
        if len(str(cardـnumber)) == 16:
            self.payment_status = True
            with open ("payment_confirmation.txt", "w") as file:
                file.write("Payment was successful!")
        else:
            self.payment_status = False
            with open ("payment_confirmation.txt", "w") as file:
                file.write("Payment was unsuccessful!")
    pass

class Factor:
    pass