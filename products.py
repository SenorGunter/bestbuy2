
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


class Non_Stock_Products(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 0)

    def show(self) -> str:
        return f"{self.name}, Price: {self.price} (Non-stocked product - no inventory tracking)"

    def buy(self, quantity) -> float:
        return float(quantity * self.price)


class Limited_Products(Product):
    def __init__(self, name, price, quantity, maximum=1):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity Limit: {self.maximum}"

    def buy(self, quantity):
        if quantity > self.maximum:
            print(f"Over the max. quantity for {self.name} \n"
                  f"Lowered to {self.maximum}")
            return self.maximum
        return float(quantity * self.price)