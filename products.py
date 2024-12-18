
class Product:

    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise ValueError

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self) -> float:
        return float(self.quantity)


    def set_quantity(self, quantity):
        if quantity >= 0:
            self.quantity = quantity
        else:
            return "Quantity has to be 0 or higher"


    def is_active(self) -> bool:
        if self.active is True:
            return True
        else:
            return False


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity) -> float:
        if quantity <= self.quantity:
            self.set_quantity((self.get_quantity() - quantity))
            if self.quantity == 0:
                self.deactivate()
            return float(quantity * self.price)
        else:
            return ValueError