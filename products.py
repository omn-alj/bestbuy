class Product:
    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid input for Product")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return "{}, Price: {}, Quantity: {}".format(self.name, self.price, self.quantity)

    def buy(self, quantity_to_buy):
        if not self.active:
            raise Exception("Product is inactive")
        if quantity_to_buy <= 0:
            raise ValueError("Invalid quantity to buy")
        if quantity_to_buy > self.quantity:
            raise Exception("Not enough quantity available")

        total_price = self.price * quantity_to_buy
        self.quantity -= quantity_to_buy

        if self.quantity == 0:
            self.deactivate()
    
        self.promotion = None  

    def get_promotion(self):
        return self.promotion

    def set_promotion(self, promotion):
        self.promotion = promotion

    def show(self):
        promo_info = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promo_info}"

    def buy(self, quantity_to_buy):
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity_to_buy)
        return super().buy(quantity_to_buy)        

class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def show(self):
        return "{}, Price: {}, Quantity: Not Applicable (Non-Stocked Product)".format(self.name, self.price)

class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity_to_buy):
        if quantity_to_buy > self.maximum:
            raise Exception("Quantity exceeds the maximum limit for this product.")
        return super().buy(quantity_to_buy)

    def show(self):
        return "{}, Price: {}, Quantity: {}, Maximum Purchase Limit: {}".format(
            self.name, self.price, self.quantity, self.maximum
        )

