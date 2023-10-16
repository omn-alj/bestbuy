from abc import ABC, abstractmethod

class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass

class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        return product.price * quantity * (1 - self.percent / 100)

class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity):
        # Apply the promotion to every 2 items, making one half price
        discounted_quantity = (quantity // 2) + (quantity % 2)
        return product.price * discounted_quantity

class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity):
        # For every 3 items, one is free
        total_price = product.price * quantity
        discounted_price = product.price * (quantity - (quantity // 3))
        return discounted_price
