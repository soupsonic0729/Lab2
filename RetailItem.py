class RetailItem:

    # Initializing
    def __init__(self):
        self.__item = "item"
        self.__units = 0
        self.__price = 0

    # Getter of Item
    def get_item(self):
        return self.__item

    # Setter of Item
    def set_item(self, item):
        self.__item = item

    # Getter of Units
    def get_units(self):
        return self.__units

    # Setter of Units
    def set_units(self, units):
        self.__units = units

    # Getter of Prices
    def get_price(self):
        return self.__price

    # Setter of Prices
    def set_price(self, price):
        self.__price = price

retail = RetailItem

# Setting r1 as Item #1
r1 = RetailItem()
r1.set_item("Jacket")
r1.set_units(12)
r1.set_price(59.95)

# Setting r1 as Item #2
r2 = RetailItem()
r2.set_item("Designer Jeans")
r2.set_units(40)
r2.set_price(34.95)

# Setting r1 as Item #3
r3 = RetailItem()
r3.set_item("Shirt")
r3.set_units(20)
r3.set_price(24.95)
