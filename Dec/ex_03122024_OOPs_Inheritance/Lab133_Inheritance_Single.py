# How to create a Class?


# Single Inheritance -> 85% of the time you will use SI in API, Web

class Father:
    key = "2BHK"

    def car(self):
        print("My father has a car --> Aulto")
        print(self.key)


class Son(Father):
    key2 = "3BHK"

    def suv(self):
        print("MG Hector , black")
        print(self.key2)


father_obj = Father()
father_obj.car()

son_obj = Son()
son_obj.suv()
