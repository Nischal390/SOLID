from abc import ABC, abstractmethod
class Pizza(ABC):
    @abstractmethod
    def get_cost(self):
        pass

    @abstractmethod
    def get_description(self):
        pass

class Margherita(Pizza):
    def get_cost(self):
        return 6.0

    def get_description(self):
        return "Margherita"

class Farmhouse(Pizza):
    def get_cost(self):
        return 8.0

    def get_description(self):
        return "Farmhouse"

class Cheese(Pizza):
    def get_cost(self):
        return 5.0

    def get_description(self):
        return "Cheese"

class ToppingDecorator(Pizza):
    def __init__(self, pizza):
        self._pizza = pizza

class CheeseTopping(ToppingDecorator):
    def get_cost(self):
        return self._pizza.get_cost()+0.5

    def get_description(self):
        return self._pizza.get_description()+" + cheese"


class Olives(ToppingDecorator):
    def get_cost(self):
        return self._pizza.get_cost() + 0.6

    def get_description(self):
        return self._pizza.get_description() + " + olives"

class Mushrooms(ToppingDecorator):
    def get_cost(self):
        return self._pizza.get_cost() + 0.4

    def get_description(self):
        return self._pizza.get_description() + " + mushrooms"

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self):
        # payment logic
        print("Payment has been made using Credit Card")


class DebitCardPayment(PaymentStrategy):
    def pay(self):
        # payment logic
        print("Payment has been made using Credit Card")


class PayPalPayment(PaymentStrategy):
    def pay(self):
        # payment logic
        print("Payment has been made using Credit Card")

class Order:
    def __init__(self, pizza):
        self.pizza = pizza
        self.payment_strategy = None

    def payment_selection(self, pay_strategy):
        self.payment_strategy = pay_strategy

    def checkout(self):
        if not self.payment_strategy:
            print("Invalid payment method. Please pay by cash")
            amount = self.pizza.get_cost()
            print(f"Order summary: {amount} USD")

        else:
            amount = self.pizza.get_cost()
            print(f"Order summary: {amount} USD")
            self.payment_strategy.pay()

if __name__ == "__main__":
    pizza = Cheese()
    pizza = Olives(pizza)
    pizza = Mushrooms(pizza)

    print(pizza.get_cost())
    print(pizza.get_description())

    order = Order(pizza)
    pay_strategy = CreditCardPayment()
    # pay_strategy = None
    order.payment_selection(pay_strategy)
    order.checkout()