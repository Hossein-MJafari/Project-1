# in this class we will determine post or peyk.
from order import *


class Logistics:
    def __init__(self, city, state, postal_code, address_detail):
        self.peyk_orders = []
        self.post_orders = []
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.address_detail = address_detail

    def assign_delivery(self):
        self.city_ID = Address(self).id().self.city_ID
        self.state_ID = Address(self).id().self.state_ID
        delivery_method = ""
        if self.state_ID == 1:
            self.peyk_orders.append(Cart.cart)
            delivery_method = "Peyk"
            print(f"Your order will be delivered by {delivery_method}.")
        else:
            self.post_orders.append(Cart.cart)
            delivery_method = "Post"
            print(f"Your order will be delivered by {delivery_method}.")
        return delivery_method


class Address():
    def __init__(self, logistics_object):
        self.state_ID = None
        self.city_ID = None
        self.state = None
        self.city = None
        self.logistic = logistics_object

    def id(self):
        if self.state == "Tehran" and self.city == 'Parand':
            self.state_ID = 1
            self.city_ID = 1
        elif self.state == "Tehran" and self.city == 'Tehran':
            self.state_ID = 1
            self.city_ID = 2
        elif self.state == "Esfahan" and self.city == 'Kashan':
            self.state_ID = 2
            self.city_ID = 1
        elif self.state == "Esfahan" and self.city == 'Khomain':
            self.state_ID = 2
            self.city_ID = 2
        elif self.state == "Tabriz" and self.city == 'Kosroshahr':
            self.state_ID = 3
            self.city = 1
        elif self.state == "Tabriz" and self.city == 'Sardorod':
            self.state_ID = 3
            self.city = 2

    def price(self):
        if self.state_ID == 1:
            self.price = 30
        else:
            self.price = 50


time_chart = {'noon': 3, 'afternoon': 3}


class Time:
    def __init__(self, delivery_time):
        self.time = delivery_time
        if self.time != 'morning':
            if time_chart[self.time] > 0:
                time_chart[self.time] = time_chart[self.time] - 1
            else:
                print('this time is not available')
                self.time = input('please enter another time:')
                if self.time != 'morning':
                    if time_chart[self.time] > 0:
                        time_chart[self.time] = time_chart[self.time] - 1
                    else:
                        print('the only time that is available is morning')
                        self.time = 'morning'
        print(f"Your estimated time is {self.time}.")