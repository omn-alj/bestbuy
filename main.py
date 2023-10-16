from products import Product, NonStockedProduct, LimitedProduct
from store import Store
from promotions import SecondHalfPrice, ThirdOneFree, PercentDiscount

def start(store_object):
    while True:
        print("Welcome to the Store Management System")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        choice = input("Enter your choice (1/2/3/4): ").strip()  # Strip whitespace

        if choice == '1':
            print("\nList of Products in Store:")
            for product in store_object.get_all_products():
                print(product.show())
            print()

        elif choice == '2':
            total_quantity = store_object.get_total_quantity()
            print("Total quantity in store: {}\n".format(total_quantity))

        elif choice == '3':
            shopping_list = []
            while True:
                product_name = input("Enter product name (or 'done' to finish): ")
                if product_name.lower() == 'done':
                    break
                product = store_object.get_product_by_name(product_name)
                if product:
                    try:
                        quantity = int(input("Enter quantity: "))
                        if quantity > 0:
                            shopping_list.append((product, quantity))
                        else:
                            print("Quantity must be greater than 0.")
                    except ValueError:
                        print("Invalid quantity. Please enter a valid number.")
                else:
                    print("Product not found in store.")

            total_cost = store_object.order(shopping_list)
            print("Order total: ${}\n".format(total_cost))

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option (1/2/3/4).\n")

if __name__ == "__main__":
    # Setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
        products.NonStockedProduct("Windows License", price=125),
        products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    ]

    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = store.Store(product_list)

    # Start the user interface
    start(best_buy)
