from wearhouse import Get_Status
import random as rand


class Cart:
    def add_to_cart(self, database: Status, product_name, size, quantity):
        self.cart = {}
        if product_name in list(database.a["stock_name"]) and size in list(database.a[database.a["stock_name"] == product_name]["size"]):
            if product_name in cart.keys():
                if size in self.cart[product_name]:
                    if quantity <= (list(database.a[(database.a["stock_name"] == product_name) & (database.a["size"] == size)]['current_stock'])[0]) - cart[product_name][size]:
                        self.cart[product_name][size] += quantity
                    else:
                        print(f"{quantity + cart[product_name][size]} number of {product_name} in size {size} is not available!")
                else:
                    cart[product_name][size] = quantity
            else:
                self.cart[product_name] = {size: quantity}
        else:
            print(f"{product_name} in size {size} is not available!")
    pass

class Payment_data:
    def __init__(self, name, phone_number, address, delivery_time):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.delivery_time = delivery_time
        self.order_ID = rand.randint((10**10), (10**11-1))
        self.payment_status = None

    def make_payment(self, card_number):
        if len(str(cardـnumber)) == 16:
            self.payment_status = True
            self.result="Payment was successful!"
            with open("payment_confirmation.txt", "w") as file:
                file.write(self.result)
        else:
            self.payment_status = False
            self.result="Payment was unsuccessful!"
            with open("payment_confirmation.txt", "w") as file:
                file.write(self.result)
    pass


class Factor:
    def __init__(self, payment_data: Payment_data, cart: Cart):
        self.payment_data = payment_data
        self.cart = cart

    pass
