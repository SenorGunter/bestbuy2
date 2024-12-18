from products import Product


class Store:
    def __init__(self, product_list: list[Product]):
        self.products: list = product_list


    def get_products(self):
        return self.products


    def add_product(self, product):
        self.get_products().append(product)


    def remove_product(self, product):
        self.get_products().remove(product)


    def get_total_quantity(self) -> int:
        total_quantities: int = 0
        for product in self.get_products():
            total_quantities += product.get_quantity()
        return total_quantities

    def get_all_products(self) -> list[Product]:
        all_products = []
        for product in self.get_products():
            if product.is_active():
                all_products.append(product)
        return all_products


    def order(self, shopping_list) -> float:
        total_cost = 0.0
        for product, order in shopping_list:
            total_cost += product.buy(order)
        return total_cost