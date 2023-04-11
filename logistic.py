#in this class we will determine post or peyk.
class Logistics:
    def __init__(self):
        self.peyk_orders = []
        self.post_orders = []
        self.city=city

    def assign_delivery(self, order):
        self.city_ID=Address().check_address(self.city)
        if self.city_ID == 1:
            self.peyk_orders.append(order)
        else::
            self.post_orders.append(order)



class Address:
    def __init__(self, city):
        self.city = city
        self.city_ID = None

    def check_address(self, Address):
        if self.city == "Tehran":
            self.city_ID = 1
        elif self.city == "Esfahan":
            self.city_ID = 2
        elif self.city == "Tabriz":
            self.city_ID = 3

    pass

class Time:
    pass

#dds