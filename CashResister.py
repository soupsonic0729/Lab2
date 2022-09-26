import RetailItem

class CashResister:

    # Initializing
    def __init__(self):
        self.__item_list = []

    # Add items to the item_list
    def purchace_item(self, retail):
        self.__item_list.append(retail)
        print("The Item Is Added To The List")

    # Return total price
    def get_total(self):
        total = 0

        for retail in self.__item_list:
            total += retail.get_price()

        return total

    # Showing purchaced item and Total price
    def show_items(self):

        for retail in self.__item_list:
            print(retail.get_item() + " " + str(retail.get_units()) + " " + str(retail.get_price()))

        print("Total: " + str(self.get_total()))

    # Remove items from list
    def clear(self):
        for retail in  self.__item_list:
            self.__item_list.remove(retail)

if __name__ == '__main__':
    item1 = RetailItem.retail()
    item2 = RetailItem.retail()
    item3 = RetailItem.retail()

    item1.set_item("Jacket")
    item1.set_units(12)
    item1.set_price(59.95)

    item2.set_item("Designer Jeans")
    item2.set_units(40)
    item2.set_price(34.95)

    item3.set_item("Shirt")
    item3.set_units(20)
    item3.set_price(24.95)

    resister = CashResister()

    resister.purchace_item(item1)
    resister.purchace_item(item2)
    resister.purchace_item(item3)

    resister.show_items()

