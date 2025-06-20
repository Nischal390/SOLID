from abc import ABC, abstractmethod
from enum import Enum

class BaseSelector(Enum):
    wheat = 'WH'
    cauliflower = "CF"
    wheat_GF = "GF"


class Pizza:
    def __init__(self, base, user):
        self.base = base
        self.topping_price = {'olives':0.5, 'mushroom':0.4, 'chicken':0.6}
        self.base_cost = {'wheat':1,'cauliflower':1.5,'wheat_GF':2}
        self.pizza_cost = self.base_cost[base]


    def add_toppings(self, topping):
        self.pizza_cost+=self.topping_price[topping]


class thincrustPizza(Pizza):
    def choose_type(pizza_type):
        



    

class User:
    def __init__(self, name):
        self.name = name
        self.pizzas = []
    
    def add_pizza(self,pizza):
        self.pizzas.append(pizza)


class Payment:
    pass

