import RetailItem

class CashResister:

    def __init__(self, item):
        self.__item_list = []
        self.item = item

    def purchace_item(self):
        self.__item_list.append(self.item)
        print("The Item Is Added To The List")

    def get_total(self):
        total = 0

        for retail in self.__item_list:
            total += retail.get_price()

        return total

    def show_items(self):

        for retail in self.__item_list:
            print(retail.get_item)
            print(retail.get_units)
            print(retail.get_price)


    def clear(self):
        self.__item_list.remove(self.item)

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

    resister1 = CashResister(item1)
    resister1.purchace_item()

    resister2 = CashResister(item2)
    resister2.purchace_item()

    resister3 = CashResister(item3)
    resister3.purchace_item()

    resister1.show_items()
    resister2.show_items()
    resister3.show_items()

