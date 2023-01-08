""" Java style code
class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negtive")
        self.__price = value
"""

# A property is an object that sits infront of an attribute
# and allows us to get or set the value


class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negtive")
        self.__price = value
    price = property(get_price, set_price)

# use decorator


class Product2:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negtive")
        self.__price = value

# read-only


class Product2:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price


product = Product(10)
print(product.price)
product.price = -1
