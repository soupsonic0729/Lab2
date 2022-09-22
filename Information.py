class Information:

    # Initializing
    def __init__(self, name, age, address, phone_num):
        self.__name = name
        self.__age = age
        self.__address = address
        self.__phone_num = phone_num

    # Getter of Name
    def get_name(self):
        return self.__name

    # Setter of Name
    def set_name(self, name):
        self.__name = name

    # Getter of Age
    def get_age(self):
        return self.__age

    # Setter of Age
    def set_age(self, age):
        self.__age = age

    # Getter of Address
    def get_address(self):
        return self.__address

    # Setter of Address
    def set_address(self, address):
        self.__address = address

    # Getter of PhoneNumber
    def get_phone_num(self):
        return self.__phone_num

    # Setter of PhoneNumber
    def set_phone_num(self, phone_num):
        self.__phone_num = phone_num

    # Setteing information objects' data in format
    def __str__(self):
        return "Name: " + str(self.__name)+ " - " + "Age: " + str(self.__age) + " - " + "Address: " + \
               str(self.__address) + " - " + "Phone: " + str(self.__phone_num)

# accepts an Information object as an argument and display
def display_info(info):
    print("Name: " + str(info.get_name()) + "\nAge: " + str(info.get_age()) + "\nAddress: " + \
               str(info.get_address()) + "\nPhone: " + str(info.get_phone_num()))

# main method
if __name__ == '__main__':
    h1 = Information("Sarah Jones", 21, "2000 Simcoe North", "+1 9123405999")
    h2 = Information("Kyoji Tanaka", 21, "1207 W 27th St.", "08097981876")

    print(h1)
    display_info(h1)

    print("\n")

    print(h2)
    display_info(h2)





