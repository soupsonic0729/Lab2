import RetailItem

class CashResister:

    def __init__(self):
        self.__item_list = []

    def purchace_item(self, retail):
        self.__item_list.append(retail)
        print("The Item Is Added To The List")

    def get_total(self):
        total = 0

        for retail in self.__item_list:
            total += retail.

        return total





