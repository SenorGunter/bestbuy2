import products
import store
import promotion

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250),
                 products.Non_Stock_Products("Windows License", price=125),
                 products.Limited_Products("Shipping", price=10, quantity=250, maximum=1)
               ]

# Create promotion catalog
second_half_price = promotion.SecondHalfPrice()
third_one_free = promotion.ThirdOneFree()
thirty_percent = promotion.PercentDiscount(30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)
best_buy = store.Store(product_list)


def menu():
    print("Store Menu \n-------\n",
          "1. List all products in Store\n",
          "2. Show total amount in Store\n",
          "3. Make an Order\n",
          "4. Quit \n-------"
          )


def list_all():
    counter = 1
    all_products = best_buy.get_products()
    for product in all_products:
        print(f"{counter}. {product.show()}")
        counter += 1
    print("-------")


def total_amount():
    return f"\nTotal of {best_buy.get_total_quantity()} items in store\n"


def make_order():
    shoppinglist = []
    print("When you want to finish order, enter empty text.")

    while True:
        product_input = input("Which product # do you want?")
        if product_input != "":
            product_id = int(product_input) - 1
            product_usable = best_buy.get_products()[product_id]
            quantity_input = input("What amount do you want?")

            # if product_usable.get_quantity() > int(quantity_input):
            shoppinglist.append((product_usable, int(quantity_input)))
            #
            # elif product_usable.get_quantity() == int(quantity_input):
            #     shoppinglist.append((product_usable, int(quantity_input)))
            #     print("The stock ran out with this order")
            #
            # else:
            #     print("Entered quantity is too great")
        else:
            break

    print(f"Order made! Total payment: {best_buy.order(shoppinglist)}")


def main():
    while True:
        list_of_commands = {"1": lambda: list_all(),
                            "2": lambda: print(total_amount()),
                            "3": lambda: (list_all(), make_order()),
                            "4": lambda: exit()}

        menu()
        user_input = input("Please choose a number: ")

        if user_input in list_of_commands:
            list_of_commands[user_input]()
        else:
            print("Input wrong")


if __name__ == "__main__":
    main()