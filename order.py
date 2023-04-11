from wearhouse import Get_Status
class Order:
    # Define an empty dictionary to store the cart items
    
    def add_to_cart(product_name, quantity):
        self.cart = {}
        if product_name in Get_Status().a["stock_name"]:
            if quantity <= Get_Status().a["current_stock"]:
                if product_name in cart:
                    cart[product_name] += quantity
                else:
                    cart[product_name] = quantity
            else:
                print(f"{quantity} of this item is  not available!")

        else:
            print("This item is not available!")


    pass

class Payment:
    pass

class Factor:
    
#ss